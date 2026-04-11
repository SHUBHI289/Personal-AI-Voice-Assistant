//   signingConfigs {
//     release {
//         keyAlias keystoreProperties['keyAlias']
//         keyPassword keystoreProperties['keyPassword']
//         storeFile keystoreProperties['storeFile'] ? file(keystoreProperties['storeFile']) : null
//         storePassword keystoreProperties['storePassword']
//     }
// }

// buildTypes {
//     release {
//         // TODO: Add your own signing config for the release build.
//         // Signing with the debug keys for now, so `flutter run --release` works.
//         signingConfig signingConfigs.release
//     }
// }
    signingConfigs {
    release {
        keyAlias keystoreProperties['keyAlias']
        keyPassword keystoreProperties['keyPassword']
        storeFile keystoreProperties['storeFile'] ? file(keystoreProperties['storeFile']) : null
        storePassword keystoreProperties['storePassword']
    }
}

buildTypes {
    release {
        // TODO: Add your own signing config for the release build.
        // Signing with the debug keys for now, so `flutter run --release` works.
        signingConfig signingConfigs.debug
        signingConfig signingConfigs.release
    }
}

// buildTypes {
//     release {
//         // TODO: Add your own signing config for the release build.
//         // Signing with the debug keys for now, so `flutter run --release` works.
//         signingConfig signingConfigs.debug
//     }
// }
}

flutter {
53 changes: 18 additions & 35 deletions53  
android/app/src/main/AndroidManifest.xml
Original file line number	Diff line number	Diff line change
@@ -1,39 +1,22 @@
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:tools="http://schemas.android.com/tools"
package="com.iycreateapp.myhostel">
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="com.google.android.gms.permission.AD_ID" tools:node="remove"/>
<application
    android:label="MyHostel"
    android:name="${applicationName}"
    android:icon="@mipmap/ic_launcher"
    android:requestLegacyExternalStorage="true">
    <activity
        android:name=".MainActivity"
        android:exported="true"
        android:launchMode="singleTop"
        android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <!-- Specifies an Android theme to apply to this Activity as soon as
<manifest xmlns:android="http://schemas.android.com/apk/res/android" xmlns:tools="http://schemas.android.com/tools" package="com.iycreateapp.myhostel">
  <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
  <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
  <uses-permission android:name="com.google.android.gms.permission.AD_ID" tools:node="remove"/>
  <application android:label="MyHostel" android:name="${applicationName}" android:icon="@mipmap/ic_launcher" android:requestLegacyExternalStorage="true">
    <activity android:name=".MainActivity" android:exported="true" android:launchMode="singleTop" android:theme="@style/LaunchTheme" android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode" android:hardwareAccelerated="true" android:windowSoftInputMode="adjustResize">
      <!-- Specifies an Android theme to apply to this Activity as soon as
                 the Android process has started. This theme is visible to the user
                 while the Flutter UI initializes. After that, this theme continues
                 to determine the Window background behind the Flutter UI. -->
            <meta-data
              android:name="io.flutter.embedding.android.NormalTheme"
              android:resource="@style/NormalTheme"
              />
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <!-- Don't delete the meta-data below.
      <meta-data android:name="io.flutter.embedding.android.NormalTheme" android:resource="@style/NormalTheme"/>
      <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
      </intent-filter>
    </activity>
    <!-- Don't delete the meta-data below.
             This is used by the Flutter tool to generate GeneratedPluginRegistrant.java -->
        <meta-data
            android:name="flutterEmbedding"
            android:value="2" />
    </application>
</manifest>
    <meta-data android:name="flutterEmbedding" android:value="2"/>
  </application>
  <uses-permission android:name="android.permission.INTERNET"/>
</manifest>
  4 changes: 2 additions & 2 deletions4  
android/build.gradle
Original file line number	Diff line number	Diff line change
@@ -1,5 +1,5 @@
buildscript {
    ext.kotlin_version = '1.6.10'
    ext.kotlin_version = '1.8.0'
    repositories {
        google()
        mavenCentral()
@@ -27,6 +27,6 @@ subprojects {
    project.evaluationDependsOn(':app')
}

task clean(type: Delete) {
tasks.register("clean", Delete) {
    delete rootProject.buildDir
}
  2 changes: 1 addition & 1 deletion2  
lib/main.dart
Original file line number	Diff line number	Diff line change
@@ -87,7 +87,7 @@ class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primaryColor: Colors.blue.shade900,
        primaryColor: Colors.teal.shade900,
        fontFamily: "Brazila",
      ),
      debugShowCheckedModeBanner: false,
  10 changes: 5 additions & 5 deletions10  
lib/presentation/screen/student/notice/StudentNoticeScreen.dart
Original file line number	Diff line number	Diff line change
@@ -5,7 +5,7 @@ import 'package:flutter/services.dart';
import 'package:grouped_list/grouped_list.dart';
import 'package:hostelapplication/logic/modules/notice_model.dart';
import 'package:hostelapplication/presentation/screen/student/studentDrawer.dart';
import 'package:image_downloader/image_downloader.dart';
// import 'package:image_downloader/image_downloader.dart';
import 'package:intl/intl.dart';
import 'package:provider/provider.dart';

@@ -113,10 +113,10 @@ class NoticeContainer extends StatelessWidget {
      case 'Save Image':
        {
          try {
            var imageId = await ImageDownloader.downloadImage(src);
            if (imageId == null) {
              return print("Image download faild");
            }
            // var imageId = await ImageDownloader.downloadImage(src);
            // if (imageId == null) {
            //   return print("Image download faild");
            // }
          } on PlatformException catch (error) {
            print(error);
          }
 336 changes: 200 additions & 136 deletions336  
pubspec.lock
Large diffs are not rendered by default.

  17 changes: 9 additions & 8 deletions17  
pubspec.yaml
Original file line number	Diff line number	Diff line change
@@ -5,7 +5,7 @@ description: A new Flutter project.
publish_to: 'none' # Remove this line if you wish to publish to pub.dev


version: 1.0.0+4
version: 1.0.0+6

environment:
  sdk: ">=2.17.3 <3.0.0"
@@ -15,26 +15,26 @@ dependencies:
  cupertino_icons: ^1.0.2
  flutter:
    sdk: flutter
  shared_preferences: ^2.0.15
  firebase_core: ^1.18.0
  firebase_auth: ^3.3.20
  cloud_firestore: ^3.1.18
  firebase_storage: ^10.2.18
  shared_preferences: 
  firebase_core: 
  firebase_auth: 
  cloud_firestore:
  firebase_storage: 
  uuid: ^3.0.6
  provider: ^6.0.3
  rflutter_alert:
  date_time_picker:
  image_picker: ^0.8.5+3
  file_picker:
  image_downloader: ^0.31.0
  # image_downloader: ^0.31.0
  file: ^6.1.4
  auto_size_text: 3.0.0
  cached_network_image: 3.2.1
  flutter_animate: 4.1.1+1
  flutter_cache_manager: 3.3.0
  font_awesome_flutter: 10.1.0
  from_css_color: 2.0.0
  google_fonts: 4.0.3
  google_fonts: 
  intl: 0.17.0
  json_path: 0.4.1
  page_transition: 2.0.4
@@ -68,6 +68,7 @@ flutter:
  assets:
    - assets/images/
    - assets/onboard/
    - shorebird.yaml

  fonts:
    - family: Brazila
 14 changes: 14 additions & 0 deletions14  
shorebird.yaml
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,14 @@
# This file is used to configure the Shorebird updater used by your app.
# Learn more at https://docs.shorebird.dev
# This file should be checked into version control.

# This is the unique identifier assigned to your app.
# Your app_id is not a secret and is just used to identify your app
# when requesting patches from Shorebird's servers.
app_id: 083f564d-803b-465f-9ad5-7e35261eade9

# auto_update controls if Shorebird should automatically update in the background on launch.
# If auto_update: false, you will need to use package:shorebird_code_push to trigger updates.
# https://pub.dev/packages/shorebird_code_push
# Uncomment the following line to disable automatic updates.
# auto_update: false
0 comments on commit feed2af
Please sign in to comment.
Footer
© 2024 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact
Manage cookies
Do not share my personal information
Copied!