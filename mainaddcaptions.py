from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


vid = VideoFileClip("video1.mp4")

# Define text, title, or caption
txt = "Thanks for watching!"
hdr = "Mera Awesome Video hai ye"
cap = "Don't forget to subscribe!"

# Create textclips , color badlana
txt_clip = TextClip(txt, fontsize=50, color='white').set_position(('center', 'bottom')).set_duration(5)  # Position text at the bottom center for 5 seconds
hdr_clip = TextClip(hdr, fontsize=70, color='white').set_position(('center', 0.2 * vid.h)).set_duration(3)  # Position title at 20% from the top for 3 seconds
cap_clip = TextClip(cap, fontsize=30, color='white').set_position(('center', 'top')).set_duration(8)  # Position caption at the top center for 8 seconds
final_vid = CompositeVideoClip([vid, txt_clip, hdr_clip, cap_clip])#nhi chl rha

# Export
final_vid.write_videofile("output_video_with_text.mp4", fps=vid.fps)

print("Video with text, title, and caption added too currebnt path")
