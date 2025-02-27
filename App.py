import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

def water1_1(input_img, output_img, text):
   original_img = Image.open(input_img).convert('RGBA')
   width, height = original_img.size
   text_image = Image.new("RGBA",(width,height),(255,255,255,0))
   text_draw = ImageDraw.Draw(text_image)
   font_size = int(width / 11)
   font = ImageFont.truetype("arial.ttf", font_size)
   x, y = int(width / 4), int(height / 2)
   text_draw.text((x, y), text, (159,159,159), font=font)
   text_image = text_image.rotate(45)
   watermark_image = Image.new("RGBA",original_img.size, (255,255,255,0))
   watermark_image.paste(text_image)
   image_with_watermark = Image.alpha_composite(original_img, watermark_image)
   image_with_watermark = image_with_watermark.convert("RGB")

   image_with_watermark.save(output_img,format="PNG")

def img1():
   path = filedialog.askopenfilename()
   entry1.delete(0, tk.END)
   entry1.insert(0, path)

def img2():
   path = filedialog.asksaveasfilename(defaultextension=".png")
   entry2.delete(0, tk.END)
   entry2.insert(0, path)

def watermark():
   path1 = entry1.get()
   path2 = entry2.get()
   text = entry3.get()
   if not path1 or not path2 or not text:
       messagebox.showerror("Error", "All fields are required!")
       return
   water1_1(path1, path2, text)
   messagebox.showinfo("Congrats", "Image saved!")

root = tk.Tk()
root.title("Image Watermark App")
root.geometry("500x500")

frame1 = tk.Frame(root)
frame1.pack(pady=20)
l1 = tk.Label(frame1, text="Image to Watermark:")
l1.pack(side="left", padx=10)
entry1 = tk.Entry(frame1, width=30)
entry1.pack(side="left")
button1 = tk.Button(frame1, text="Select", width=20, command=img1)
button1.pack(side="right", padx=10)

frame2 = tk.Frame(root)
frame2.pack(pady=20)
l2 = tk.Label(frame2, text="Save Watermarked Image")
l2.pack(side="left", padx=10)
entry2 = tk.Entry(frame2, width=30)
entry2.pack(side="left")
button2 = tk.Button(frame2, text="Select", width=20, command=img2)
button2.pack(side="right", padx=10)

frame3 = tk.Frame(root)
frame3.pack(pady=20)
l3 = tk.Label(frame3, text="Enter text")
l3.pack(side="left", padx=10)
entry3 = tk.Entry(frame3, width=30)
entry3.pack(side="left")
button3 = tk.Button(root, width=20, text="Watermark", command=watermark)
button3.pack(expand=True)

root.mainloop()
