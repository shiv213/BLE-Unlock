[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# BLE-Unlock
Unlocks and locks Linux based system if configured BLE device is close in proximity.

Using [GATT SDK](https://github.com/getsenic/gatt-python)

### To Install:
- Clone the repository `git clone https://github.com/shiv213/BLE-Unlock.git`
- Install the Python dependencies `pip install -r requirements.txt`
- Run `sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0`
- Edit lines 7-8 of the `main.py` file to set the BLE device's MAC address, how many attempts to try before locking and how long to wait between attempts.

### To Run:
```shell
sudo ./main.py
```

## Contributing
Contributions are welcome via pull requests/[issues](https://github.com/shiv213/BLE-Unlock/issues).

## Support
<a href="https://www.buymeacoffee.com/shivvtrivedi" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
<p>Or</p> 

<a href="https://www.patreon.com/shivvtrivedi">
	<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)