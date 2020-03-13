# pyPhotos
Sync media files to Google Photos on Android without Google Play Services. Based on [eshmu's gphotos-upload](https://github.com/eshmu/gphotos-upload).

## Setup

### 1. Obtaining a Google Photos API key

Obtain a Google Photos API key (Client ID and Client Secret) by following the instructions on [Getting started with Google Photos REST APIs](https://developers.google.com/photos/library/guides/get-started)

**NOTE** When selecting your application type in Step 4 of "Request an OAuth 2.0 client ID", please select "Other". There's also no need to carry out step 5 in that section.


### 2. Setup client_id.json 
   On your PC, right click and "Save Link as..." [this link](https://github.com/marcalv/pyPhotos/raw/master/resources/client_id.json) to download client_id.json template to your PC. Then:
   * Replace `YOUR_CLIENT_ID` in the *client_id.json* file with the provided Client ID. 
   * Replace `YOUR_CLIENT_SECRET` in the *client_id.json* file wiht the provided Client Secret.
  
  Copy *client_id.json* to the storage root of your Android device. (You can also copy auth.txt only in case you have already generated a valid one.)

### 3. Install Termux
Install [Termux](https://f-droid.org/app/com.termux) and [Termux:Widget](https://f-droid.org/app/com.termux.widget) (optional, highly recommended) on your Android device.
### 4. Install pyPhotos
Open Termux and run the following command:
```
pkg install git -y && git clone https://github.com/marcalv/pyPhotos && cd pyPhotos && chmod +x setup.sh && ./setup.sh && exit
```
This script will:
* Install all necesary packages and dependencies to run pyPhotos. 
* Move from the root of your internal storage *client_id.json* or *auth.txt* to pyPhotos installation folder (*~/pyPhotos*). 
* Setup a termux shortcut. You will be able to run pyPhotos from your launcher with [Termux:Widget](https://f-droid.org/app/com.termux.widget) without typing anything.
* Restart Termux after installation is completed
 
 ### 5. Test run
Remember to **restart termux after installation** if it does not do it automatically.
1. Run ```pyphotos auth``` command to create an *auth.txt* file from the credentials in *client_id.json*. In this case it will ask you to open an url and log in with your Google account. Accept asked permissions and ignore warnings prompted (unverified app). 

    You can save this auth.txt file to use it in another installation and skip this step.

2. Test pyphotos with  ```pyphotos test``` command to upload a sample picture.

 ### 5. First backup
1. Customize *foldes.py* with your own preferences. This files contains an array with folder paths to sync. You can navigate with termux to get folder paths. Useful commands: ```cd ~/storage/shared/``` and ```pwd``` (print working directory)
2. Run ```pyphotos``` command to start backing up folders declared in folders.py.

*db.json* file stores wich media files have been backed up. Initially this database is empty. In some situations (after accidentally uninstalling termux, for example) you wouldn't want to upload all your media again, as *db.json* is empty. Instead, you can run ```pyphotos abu``` (all backed up) to update your local db to the current state of targeted folders without upload anything. In any case, Google Servers won't store duplicated media. It's clever enough to not save it, but upload will occur.

 ### 6. Widget Setup (optional)
You can add a widget to your home page if you have [Termux:Widget](https://f-droid.org/app/com.termux.widget) installed following these steps:

1. Add a widget to your home screen as you would normally do.
2. There are two available Termux widgets, one is a list of current shortcuts installed, and the other is a shortcut to an specific shortcut. In both cases you'll see launch_pyphotos.sh.
3. Anytime you want to start backing up, use these widgets.
