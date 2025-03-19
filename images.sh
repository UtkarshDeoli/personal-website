#!/bin/bash

# Paths
POSTS_DIR="/home/utkarsh/Documents/UtkarshDeoli/010 Blogs"
ATTACHMENTS_DIR="/home/utkarsh/Documents/UtkarshDeoli/images"
STATIC_IMAGES_DIR="/home/utkarsh/Documents/Projects/personal-website/static/images"

# Ensure the static images directory exists
mkdir -p "$STATIC_IMAGES_DIR"

echo "Start"

# Step 1: Find and process each markdown file in the posts directory (including subdirectories)
find "$POSTS_DIR" -type f -name "*.md" | while read -r file; do
    echo "Processing: $file"

    # Read the content of the Markdown file
    content=$(<"$file")

    # Step 2: Find all image links in the format `![[Pasted image ...]]`
    images=$(grep -oP '!\[\[\K[^]]*\.png(?=]])' "$file")

    # Step 3: Replace image links and copy images
    for image in $images; do
        # Create the Markdown-compatible image link
        markdown_image="![Image Description](/images/${image// /%20})"
        content="${content//"![[${image}]]"/$markdown_image}"

        # Step 4: Copy the image to the Hugo static/images directory
        image_source="$ATTACHMENTS_DIR/$image"
        image_destination="$STATIC_IMAGES_DIR/$image"

        if [[ -f "$image_source" ]]; then
            cp "$image_source" "$image_destination"
            echo "Copied: $image_source -> $image_destination"
        else
            echo "Image not found: $image_source"
        fi
    done

    # Step 5: Write the updated content back to the Markdown file
    echo "$content" > "$file"
done

echo "Markdown files processed and images copied successfully."
