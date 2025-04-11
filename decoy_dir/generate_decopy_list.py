import os
import argparse

def generate_decoy_list(pdb_id, frame_dir, output_file="decoy_list.txt"):
    # List all PDB files in the directory, sorted for consistency
    frame_files = sorted(f for f in os.listdir(frame_dir) if f.endswith(".pdb"))

    if not frame_files:
        raise ValueError(f"No .pdb files found in directory: {frame_dir}")

    with open(output_file, "w") as out:
        for fname in frame_files:
            out.write(f"{pdb_id} {fname}\n")
    
    print(f"Decoy list written to {output_file} with {len(frame_files)} entries.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a decoy list from frame PDB files.")
    parser.add_argument("pdb_id", help="PDB ID to prepend to each frame entry.")
    parser.add_argument("frame_dir", help="Directory containing the frame_XXX.pdb files.")
    parser.add_argument("--output_file", default="decoy_list.txt", help="Path to output .txt file.")

    args = parser.parse_args()
    generate_decoy_list(args.pdb_id, args.frame_dir, args.output_file)
