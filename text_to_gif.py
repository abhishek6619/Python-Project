from PIL import Image, ImageDraw, ImageFont
import imageio
import os

def text_to_gif(text, gif_name, output_folder="generated_gifs", font_size=40, frame_count=20):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    frames = []
    width, height = 500, 300  # Increased size for better visuals
    font = ImageFont.load_default()
    
    for i in range(frame_count):
        img = Image.new("RGB", (width, height), (30, 30, 30))  # Dark background
        draw = ImageDraw.Draw(img)
        text_position = (50, 130)
        animated_text = text[:max(1, (i * len(text)) // frame_count)]
        draw.text(text_position, animated_text, font=font, fill=(255, 255, 255))  # White text
        
        # Adding a border effect
        draw.rectangle([(40, 120), (width - 40, height - 120)], outline=(255, 0, 0), width=2)
        frames.append(img)
    
    output_path = os.path.join(output_folder, f"{gif_name}.gif")
    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
    print(f"GIF saved as {output_path}")

if __name__ == "__main__":
    user_text = input("Enter a sentence: ")
    gif_name = input("Enter GIF name: ")
    text_to_gif(user_text, gif_name)
