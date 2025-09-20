QR Code Generator in Python
📌 Overview

This Python project allows you to generate QR codes for multiple profiles or links, such as LinkedIn, LeetCode, and Kaggle.
The generated QR codes can be customized with colors, sizes, borders, and even gradient effects.
It’s perfect for sharing your digital profiles on resumes, business cards, or presentations.

🔹 Features
-->Generate individual QR codes for each profile.
-->Generate a combined QR code containing all links.
-->Customize QR codes with:
-->Colors (fill_color, back_color)
-->Styles (rounded or square modules)
-->Box size and border thickness
-->Gradient effects
-->High error correction for reliable scanning.

🔹 Requirements : Python 3.x

 Libraries : qrcode , pillow

Install dependencies using:

      pip install qrcode[pil]

🔹 How to Use

      Edit your profile links in the my_qrcode_editor.py file:

      profiles = {
          "LinkedIn": "https://www.linkedin.com/in/your-username",
          "LeetCode": "https://leetcode.com/your-username",
          "Kaggle": "https://www.kaggle.com/your-username"
      }


Run the script:

      python my_qrcode_editor.py


Output:
  
      Individual QR codes saved as:

        LinkedIn_qr.png
        LeetCode_qr.png
        Kaggle_qr.png


Combined QR code saved as:

        All_Profiles_QR.png


Scan with any QR code scanner or smartphone camera to open your profiles.

🔹 Customization

      You can adjust:

          Style: "rounded" or "square" modules

Colors: fill_color, back_color

Size: box_size and version

Gradient: gradient=True or False

Error correction: High (H) ensures scanning even if partially damaged.

🔹 Example
      create_qr(
          data="https://www.linkedin.com/in/your-username",
          filename="LinkedIn_qr.png",
           style="rounded",
          gradient=True,
          fill_color="blue",
          back_color="white"
      )

🔹 Notes
Make sure the file name is not qrcode.py, otherwise it will conflict with the library.
Works best in Python 3 environments with qrcode[pil] installed.
