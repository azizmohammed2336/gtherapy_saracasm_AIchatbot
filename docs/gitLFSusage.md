# Git LFS and This Project

## What is Git LFS?
Git Large File Storage (Git LFS) is a Git extension used to manage large files such as:
- machine learning model weights
- `.safetensors` files
- `.bin` checkpoints
- large datasets

Instead of storing the full file directly in Git history, Git LFS stores a small pointer file in the repository and keeps the real large file in separate LFS storage.

## Why Git LFS is needed for this project
This project includes large AI model files that are too big for normal GitHub limits.

Examples from this project:
- `sarcasmclassifier/final/model.safetensors`
- classifier and LoRA model artifacts

GitHub rejects files larger than 100 MB in normal Git commits, so Git LFS is used to:
- keep the project on GitHub
- preserve model files
- avoid push failures from large files
- make it possible to share the project with full model history

## How Git LFS works in this project
When the project is pushed:
- small code files are stored normally in Git
- large model files are tracked by Git LFS
- collaborators clone the repo and Git LFS downloads the real model files automatically

## How a general user can use Git LFS

### 1. Install Git LFS
On Mac:
```bash
brew install git-lfs
git lfs install
```

### 2. Clone the repository
```bash
git clone <repo-url>
cd finalProject
```

### 3. Download LFS files
If the repo includes LFS-tracked files, Git LFS will fetch them automatically during clone.  
If needed, run:
```bash
git lfs pull
```

### 4. Check which files use LFS
```bash
git lfs ls-files
```

## How to add a large file with Git LFS
If a user wants to add a large model file:
```bash
git lfs track "*.safetensors"
git add .gitattributes
git add path/to/large-model.safetensors
git commit -m "Add model with Git LFS"
git push origin main
```

## Important notes
- Git LFS is best for large binaries, not source code.
- Code files should remain normal Git files.
- Large files must be tracked with LFS before committing.
- If a large file was already committed normally, the history may need to be rewritten.

## Summary
Git LFS is essential for this project because it allows large AI model files to be stored and shared through GitHub without exceeding file size limits. It keeps the repository usable while still preserving the trained classifier and LoRA model artifacts.
