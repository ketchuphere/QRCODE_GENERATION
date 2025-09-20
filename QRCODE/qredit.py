import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask

# CONFIGURATION
# ------------------------------
profiles = {
    "LinkedIn": "https://www.linkedin.com/in/your-username",
    "LeetCode": "https://leetcode.com/your-username",
    "Kaggle": "https://www.kaggle.com/your-username"
}

# FUNCTIONS
# ------------------------------
def create_qr(
    data,
    filename="qrcode.png",
    version=2,
    box_size=12,
    border=4,
    style="rounded",
    gradient=False,
    fill_color="black",
    back_color="white"
):
    """
    Generate a customizable QR code.

    Args:
        data (str): Text or link to encode
        filename (str): Output filename
        version (int): Size control (1–40, higher = bigger QR)
        box_size (int): Size of each module (pixel block)
        border (int): Thickness of white border
        style (str): 'rounded' or 'square' style
        gradient (bool): Enable radial gradient
        fill_color (str/tuple): Module color
        back_color (str/tuple): Background color
    """
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Choose module style
    module_style = RoundedModuleDrawer() if style == "rounded" else SquareModuleDrawer()

    # Choose color style
    if gradient:
        color_mask = RadialGradiantColorMask(
            back_color=back_color,
            center_color=(0, 102, 204),  # blue center
            edge_color=(0, 0, 0)         # black edges
        )
    else:
        color_mask = SolidFillColorMask(back_color=back_color, front_color=fill_color)

    # Create styled QR code
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=module_style,
        color_mask=color_mask,
    )

    img.save(filename)
    print(f"✅ QR code saved as {filename}")



# USAGE EXAMPLES
# ------------------------------
if __name__ == "__main__":
    # 1. Generate individual QR codes for each profile
    for name, url in profiles.items():
        create_qr(
            url,
            filename=f"{name}_qr.png",
            style="rounded",
            gradient=True
        )

    # 2. Generate a combined QR code with all links
    combined_text = "\n".join([f"{name}: {url}" for name, url in profiles.items()])
    create_qr(
        combined_text,
        filename="All_Profiles_QR.png",
        style="square",
        gradient=False,
        fill_color="darkgreen",
        back_color="white"
    )
