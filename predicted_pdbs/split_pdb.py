import MDAnalysis as mda
import os
import argparse

def extract_frames(input_pdb, output_dir):
    # Load the multi-frame PDB file
    u = mda.Universe(input_pdb)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop over all frames and write each to a separate file
    for ts in u.trajectory:
        frame_index = ts.frame
        output_path = os.path.join(output_dir, f"frame_{frame_index:03d}.pdb")
        with mda.Writer(output_path, multiframe=False) as writer:
            writer.write(u.atoms)
        print(f"Written: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split multi-frame PDB into separate PDB files for each frame.")
    parser.add_argument("input_pdb", help="Path to the input multi-frame PDB file.")
    parser.add_argument("output_dir", help="Directory to save the output PDB files.")

    args = parser.parse_args()
    extract_frames(args.input_pdb, args.output_dir)
