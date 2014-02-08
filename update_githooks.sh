#!/bin/bash
# Update the git hooks
# Use this script instead of doing the cp manually incase there's anything else that needs to be done during the updating of the git hooks


current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
src_dir=$current_dir/hooks
dest_dir=$current_dir/../.git/hooks

cp $src_dir/* $dest_dir

pip install -r $current_dir/requirements.txt
