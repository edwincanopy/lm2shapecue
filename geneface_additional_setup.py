# run this in the GeneFacePlusPlus directory

# note here we removed the code replacing c++14 with c++17
import glob
all_files = glob.glob("GeneFacePlusPlus/modules/radnerfs/*.py") + glob.glob("GeneFacePlusPlus/modules/radnerfs/*/*.py") + glob.glob("GeneFacePlusPlus/modules/radnerfs/*/*/*.py") + glob.glob("GeneFacePlusPlus/modules/radnerfs/*/*/*/*.py")
for file in all_files:
  with open(file) as f:
    lines = f.readlines()
    lines = [line.replace('-std=c++14', '-std=c++17') for line in lines]
    lines = [line.replace('\'-use_fast_math\'', '') for line in lines]
    if 'backend' in file:
      print(lines)
  with open(file, 'w') as f:
    f.writelines(lines)

# build extensions - do we need to re-run this?
# bash docs/prepare_env/install_ext.sh
