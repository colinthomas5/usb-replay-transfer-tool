# usb_replay_transfer_tool
Python script to mass transfer all Slippi replays (*.slp format) from connected external drives to a folder on the desktop. This script is intended to transfer replays created on Wii consoles by Slippi-Nintendont.

## Prerequisites
Python3 is required to run the usb_replay_transfer_tool script.

For a drive to be recognized by usb_replay_transfer_tool, the following contents must be at the root of the drive:
```
* Folder named "Slippi"
  * This should already be on the drive due to Slippi-Nintendont creating this folder and saving all replays to this folder
* File named "setup.info"
  * This will be a file with the text "station=", followed by the number indicating the station that the external drive is used at
    * For the stream station(s), use "station=0"
```

## Usage
Upon running the script, you will be prompted to name the folder that the replays will be copied into. This folder will be created within a new folder on the desktop named "Console Slippi Replays". After all drives have been recognized and all replays have been copied over, the script will prompt you asking if you want to delete the replays from the external drives.

## Contact
If you have any feature suggestions or find any bugs, here is where you can find me

```
• Twitter: @chatterteethsrc
• Discord: chatterteeth
```

## License
This project is licensed under the [MIT](LICENSE) license.
