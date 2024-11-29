---
title: Recipe for auto blogs (Obsidian + Hugo)
Date: 2024-11-29
draft: false
---
## What is Obsidian ?

Obsidian is a powerful, privacy-focused note-taking and knowledge management app designed for building a personal knowledge base. It uses plain text Markdown files stored locally, giving users complete ownership and control over their data. With its extensive customization options, plugins, and graph view, Obsidian excels at linking and visualizing ideas, making it an ideal tool for creative thinkers, researchers, and writers. Its offline functionality ensures seamless access to notes without relying on cloud services.

![Image Description](/images/Pasted%20image%2020241129143042.png)
This is currently my obsidian vault, People use it as their second brain, and it has some cool features to represent your notes here is a example for my obsidian vault.

But you can use it to automate your hugo blog website. Credits to network chuck for the idea.

## What is hugo tho ?
oh ya i forgot to tell you what hugo is . So hugo is a basic CMS written in go used for generating static sites. you can use premade themes with hugo and add your content and wallah you have a website .

### How do i setup my hugo website ?
#### **1. Install Hugo**

- **On Linux**:
    
    
    
    `sudo apt install hugo`
    
    Alternatively, use the official Hugo documentation to install the latest version.
    
- **On macOS**:
    
    
    
    `brew install hugo`
    
- **On Windows**:  
    Download the binary from the [Hugo releases page](https://github.com/gohugoio/hugo/releases).
    

Check the version to ensure it's installed:


`hugo version`

---
#### **2. Create a New Hugo Site**

Run the following command to create a new Hugo site:



`hugo new site my-website`

This creates a directory structure for your site in `my-website`.

---

#### **3. Add a Theme**

Browse Hugo themes at themes.gohugo.io and choose one.

- **Add a theme using Git:**
    `cd my-website git init git submodule add https://github.com/your-chosen-theme-repo themes/your-theme-name`
- **Set the theme in `config.toml`:**
    `theme = "your-theme-name"

---

#### **4. Add Content**

- Create a new post:
	`hugo new posts/my-first-post.md`
- Edit the file in the `content/posts/` directory:
	`--- title: "My First Post" date: 2024-11-29 draft: true --- Write your content here.`
---

#### **5. Preview the Website Locally**

Run the Hugo development server:


`hugo server -D`

Visit http://localhost:1313 to preview your site.

---

#### **6. Build the Site**

Generate the static files for deployment:


`hugo`

The output will be in the `public/` directory.

---

#### **7. Deploy the Site**

Choose a hosting service (e.g., GitHub Pages, Netlify, or Vercel).

#### **Deploying on GitHub Pages:**

1. Initialize a Git repository in your Hugo site directory:
    
 
    
    `git init`
    
2. Add the generated `public/` folder as a Git subtree or separate branch.

    
    `git add . git commit -m "Initial commit"`
    
3. Push to GitHub.

#### **Deploying on Netlify:**

1. Drag the `public/` folder into your Netlify dashboard.
2. Configure build settings:
    - Build Command: `hugo`
    - Publish Directory: `public`

---

#### **8. Customize Your Site**

- Edit the `config.toml` file to set site-wide settings:
    
    
    `baseURL = "https://your-site-url.com/" languageCode = "en-us" title = "My Hugo Site" theme = "your-theme-name"`
    
- Add static files (e.g., images) to the `static/` directory.
    
- Use shortcodes for additional functionality (like embedding YouTube videos or tweets).
    

---

#### **9. Enhance Your Site**

- Install plugins or enable features like tags, categories, or pagination.
- Use custom CSS and layouts in the `layouts/` folder for more control.

---


## How do i setup the auto deploy blog 
For now watch the original content [here](https://www.youtube.com/watch?v=dnE7c0ELEH8&ab_channel=NetworkChuck)
I will soon make a video or just complete the blog to instruct you further as he uses the hostinger because he got them as a sponcer. But you can just use the Firebase to deploy your hugo website.
I have also used that only.