import os
import re
import shutil

# Paths
posts_dir = "/home/utkarsh/Documents/UtkarshDeoli/010 Blogs"
attachments_dir = "/home/utkarsh/Documents/UtkarshDeoli/images"
static_images_dir = "/home/utkarsh/Documents/Projects/personal-website/static/images"

# Ensure the static images directory exists
os.makedirs(static_images_dir, exist_ok=True)

print('Start')

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        # Read the content of the Markdown file
        with open(filepath, "r") as file:
            content = file.read()
            print('Iterate')
        # Step 2: Find all image links in the format `![[Pasted image ...]]`
        images = re.findall(r'!\[\[([^]]*\.png)\]\]', content)
        print(images)
        # Step 3: Replace image links with the correct format
        for image in images:
            # Create the Markdown-compatible image link
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"![[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory
            image_source = os.path.join(attachments_dir, image)
            image_destination = os.path.join(static_images_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, image_destination)
                print(f"Copied: {image_source} -> {image_destination}")
            else:
                print(f"Image not found: {image_source}")

        # Step 5: Write the updated content back to the Markdown file
        with open(filepath, "w") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")

