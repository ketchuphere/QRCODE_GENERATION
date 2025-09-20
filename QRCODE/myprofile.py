import qrcode
from PIL import Image


# Your profile links
profiles = {
    "LinkedIn": "https://www.linkedin.com/in/keshav-chawda-471a54275/",
    "LeetCode": "https://leetcode.com/u/ketchup__/",
    "Kaggle": "https://www.kaggle.com/keshavchawda"
}

# Option 1: Generate separate QR codes for each profile
for name, url in profiles.items():
    img = qrcode.make(url)
    img.save(f"{name}_qrcode.png")
    print(f"{name} QR code saved as {name}_qrcode.png")

# Option 2: Generate one QR code with all links together
combined_text = "\n".join([f"{name}: {url}" for name, url in profiles.items()])
combined_img = qrcode.make(combined_text)
combined_img.save("All_Profiles_QR.png")
print("Combined QR code saved as All_Profiles_QR.png")

