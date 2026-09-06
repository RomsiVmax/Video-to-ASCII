# Video to ASCII

**Video to ASCII** is an open-source software made by me for converting video to ASCII.
 
 
 ### What's already implemented

  - Converter for mp4 to ASCII (saved in json format)
  - Working audio conversion (gets saved in wave format)
  - Renderer for the ASCII video (plays audio too)


### What will be implemented
  - Better way for specifying input video
  - Better way to export the .json and .wav file
  - Better audio format

### How it works

  First of all, the converter takes the input video                             
  and uses a modified version of audio-extract                                    
  0.7.0 by riad-azz to extract the audio out of the                               
  video. Secondly, the converter takes the input                           
  video and uses the library moviepy to convert it                    
  into a gray video (because ASCII has no color).                    
  Then, the frames of the video get saved as                   
  pictures, which get converted into a json file                
  with all grayscale values. Lastly, they get                 
  mapped to the corresponding ASCII character.            
                                                   
  ### How to use                                   
                                                   
  Rename the video file to "source.mp4" and copy it           
  to "ascii/". Then, launch "!launch_converter.bat"            
  and wait until it EXPLICITLY says is's done.             

  If you then launch "!launch_ascii_renderer.bat",      
  the ASCII video will render. If you only need    
  the video and audio, the outputs are named    
  "sound.wav" and "ascii.json". They get saved    
  in "ascii/".                                 
