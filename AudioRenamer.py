import os
import shutil



desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
audio_dir = os.path.join(desktop_path, 'AudioInput')

audio_files = os.listdir(audio_dir)

template = "VBS1_{trial}_{type}_{run}_{pre/post}.wav"

run1b = "24_segments"
run2b = "20_segments"
run3b = "35_segments"
run1a = "50_pre_segments"
run2a = "39_pre_segments"
run3a = "47_pre_segments"

# handles directory creation
headFolder = "AG Organized Audio"
subject = "AG"

os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Bpress_equivalent")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN1")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN1/{subject}_Bv_RUN1_post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN1/{subject}_Gl_RUN1_post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN1/{subject}_Hv_RUN1_post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN2")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN2/{subject}_Bv_RUN2_post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN2/{subject}_Gl_RUN2_post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN2/{subject}_Hv_RUN2_post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN3")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN3/{subject}_Bv_RUN3_post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN3/{subject}_Gl_RUN3_post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN3/{subject}_Hv_RUN3_post")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN1")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN1/{subject}_Bv_RUN1_pre")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN1/{subject}_Gl_RUN1_pre")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN1/{subject}_Hv_RUN1_pre")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN2")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN2/{subject}_Bv_RUN2_pre")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN2/{subject}_Gl_RUN2_pre")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN2/{subject}_Hv_RUN2_pre")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN3")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN3/{subject}_Bv_RUN3_pre")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN3/{subject}_Gl_RUN3_pre")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN3/{subject}_Hv_RUN3_pre")

os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/{subject}_HighVowels")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/{subject}_BackVowels")
os.makedirs(f"/Users/coleman/Desktop/AudioInput/{headFolder}/{subject}_Glides")


for filename in audio_files:
    print(filename)

    # handles renaming files
    if filename.endswith("segments"):
        for item in os.listdir(os.path.join(audio_dir, filename)):
            templateCopy = template
            if item.endswith(".wav"):
                # print(item)

                # handles the run number and pre/post
                if filename.endswith(run1b):
                    templateCopy = templateCopy.replace("{run}", "run1")
                    templateCopy = templateCopy.replace("{pre/post}", "post")
                elif filename.endswith(run2b):
                    templateCopy = templateCopy.replace("{run}", "run2")
                    templateCopy = templateCopy.replace("{pre/post}", "post")
                elif filename.endswith(run3b):
                    templateCopy = templateCopy.replace("{run}", "run3")
                    templateCopy = templateCopy.replace("{pre/post}", "post")
                elif filename.endswith(run1a):
                    templateCopy = templateCopy.replace("{run}", "run1")
                    templateCopy = templateCopy.replace("{pre/post}", "pre")
                elif filename.endswith(run2a):
                    templateCopy = templateCopy.replace("{run}", "run2")
                    templateCopy = templateCopy.replace("{pre/post}", "pre")
                elif filename.endswith(run3a):
                    templateCopy = templateCopy.replace("{run}", "run3")
                    templateCopy = templateCopy.replace("{pre/post}", "pre")

                # handles trial type
                if item.endswith("glide.wav"):
                    templateCopy = templateCopy.replace("{type}", "Gl")
                elif item.endswith("backv.wav"):
                    templateCopy = templateCopy.replace("{type}", "Bv")
                elif item.endswith("highv.wav"):
                    templateCopy = templateCopy.replace("{type}", "Hv")

                # handles trial number
                index = item.find("_T") + 1
                # accounts for glitch in single digit naming
                if item[index+2] == "_":
                    oldItem = item
                    item = item[:index+1] + "0" + item[index+1:]
                    os.rename(os.path.join(os.path.join(audio_dir, filename), oldItem), os.path.join(os.path.join(audio_dir, filename), item))
                trialNumber = item[index:(index+3)]
                templateCopy = templateCopy.replace("{trial}", trialNumber)

                # renames files and slots into directories
                # print(templateCopy)
                runFolder = os.path.join(audio_dir, filename)
                itemFile = os.path.join(runFolder, item)
                itemFileRenamed = os.path.join(runFolder, templateCopy)
                # renames file in same spot
                os.rename(itemFile, itemFileRenamed)

                # copies into new folder where appropriate
                if "run1_post" in templateCopy:
                    shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN1")
                    if "Hv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN1/{subject}_Hv_RUN1_post")
                    elif "Gl" in templateCopy: 
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN1/{subject}_Gl_RUN1_post")
                    elif "Bv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN1/{subject}_Bv_RUN1_post")
                elif "run2_post" in templateCopy:
                    shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN2")
                    if "Hv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN2/{subject}_Hv_RUN2_post")
                    elif "Gl" in templateCopy: 
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN2/{subject}_Gl_RUN2_post")
                    elif "Bv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN2/{subject}_Bv_RUN2_post")
                elif "run3_post" in templateCopy:
                    shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN3")
                    if "Hv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN3/{subject}_Hv_RUN3_post")
                    elif "Gl" in templateCopy: 
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN3/{subject}_Gl_RUN3_post")
                    elif "Bv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Post/RUN3/{subject}_Bv_RUN3_post")
                elif "run1_pre" in templateCopy:
                    shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN1")
                    if "Hv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN1/{subject}_Hv_RUN1_pre")
                    elif "Gl" in templateCopy: 
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN1/{subject}_Gl_RUN1_pre")
                    elif "Bv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN1/{subject}_Bv_RUN1_pre")
                elif "run2_pre" in templateCopy:
                    shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN2")
                    if "Hv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN2/{subject}_Hv_RUN2_pre")
                    elif "Gl" in templateCopy: 
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN2/{subject}_Gl_RUN2_pre")
                    elif "Bv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN2/{subject}_Bv_RUN2_pre")
                elif "run3_pre" in templateCopy:
                    shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN3")
                    if "Hv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN3/{subject}_Hv_RUN3_pre")
                    elif "Gl" in templateCopy: 
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN3/{subject}_Gl_RUN3_pre")
                    elif "Bv" in templateCopy:
                        shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/Pre/RUN3/{subject}_Bv_RUN3_pre")

                if "Hv" in templateCopy:
                    shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/{subject}_HighVowels")
                elif "Bv" in templateCopy:
                    shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/{subject}_BackVowels")
                elif "Gl" in templateCopy:
                    shutil.copy(itemFileRenamed, f"/Users/coleman/Desktop/AudioInput/{headFolder}/{subject}_Glides")

