name: Build Android

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      # Checkout
      - name: Checkout
        uses: actions/checkout@v4

      # Python
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      # Java
      - name: Setup Java
        uses: actions/setup-java@v4
        with:
          distribution: "temurin"
          java-version: "17"

      # Cache Buildozer
      - name: Cache Buildozer
        uses: actions/cache@v3
        with:
          path: |
            ~/.buildozer
            .buildozer
          key: ${{ runner.os }}-buildozer-${{ hashFiles('buildozer.spec') }}

      # Linux dependencies
      - name: Install dependencies
        run: |
          sudo apt-get update

          sudo apt-get install -y \
            build-essential \
            git \
            zip \
            unzip \
            openjdk-17-jdk \
            python3-pip \
            autoconf \
            libtool \
            pkg-config \
            zlib1g-dev \
            libncurses5-dev \
            libncursesw5-dev \
            libtinfo5 \
            cmake \
            libffi-dev \
            libssl-dev \
            wget \
            curl \
            tar

          pip install --upgrade pip
          pip install cython==0.29.33 buildozer

      # Android SDK cmdline-tools
      - name: Install Android cmdline-tools
        run: |
          mkdir -p $HOME/android-sdk/cmdline-tools

          cd $HOME/android-sdk

          wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O cmdline-tools.zip

          unzip -q cmdline-tools.zip

          mv cmdline-tools latest-temp

          mkdir -p cmdline-tools

          mv latest-temp cmdline-tools/latest

          echo "ANDROID_HOME=$HOME/android-sdk" >> $GITHUB_ENV
          echo "ANDROID_SDK_ROOT=$HOME/android-sdk" >> $GITHUB_ENV

          mkdir -p ~/.buildozer/android/platform/android-sdk/tools/bin

          ln -sf \
            $HOME/android-sdk/cmdline-tools/latest/bin/sdkmanager \
            ~/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager

      # Accept Android licenses
      - name: Accept Android licenses
        run: |
          mkdir -p ~/.android

          yes | $HOME/android-sdk/cmdline-tools/latest/bin/sdkmanager --licenses || true

      # Install Android packages
      - name: Install Android SDK packages
        run: |
          $HOME/android-sdk/cmdline-tools/latest/bin/sdkmanager \
            "platform-tools" \
            "platforms;android-33" \
            "build-tools;33.0.2"

      # Environment variables
      - name: Set Android environment
        run: |
          echo "ANDROID_HOME=$HOME/android-sdk" >> $GITHUB_ENV
          echo "ANDROID_SDK_ROOT=$HOME/android-sdk" >> $GITHUB_ENV
          echo "PATH=$PATH:$HOME/android-sdk/platform-tools" >> $GITHUB_ENV

      # Build APK
      - name: Build APK
        run: |
          buildozer android release

      # Upload artifact
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: android-build
          path: bin/*.apk
