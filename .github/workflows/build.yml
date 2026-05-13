name: Build Android APK

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          sudo apt update

          sudo apt install -y \
            zip \
            unzip \
            openjdk-17-jdk \
            autoconf \
            libtool \
            pkg-config \
            zlib1g-dev \
            libncurses5-dev \
            libncursesw5-dev \
            cmake \
            libffi-dev \
            libssl-dev \
            git \
            build-essential \
            ccache

      - name: Install Python tools
        run: |
          python -m pip install --upgrade pip setuptools wheel

          pip install cython==0.29.36
          pip install buildozer==1.5.0

          # IMPORTANTE:
          # versión moderna compatible con AAB
          pip install python-for-android==2024.1.21

      - name: Accept Android licenses
        run: |
          mkdir -p ~/.android
          touch ~/.android/repositories.cfg

      - name: Clean previous builds
        run: |
          buildozer android clean

      - name: Build APK
        run: |
          buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: android-apk
          path: bin/*.apk
