import pandas as pd


def aggregate(outfilepath1, outfilepath2, infilepath1, infilepath2):
    csv1 = pd.read_csv(outfilepath1)
    csv2 = pd.read_csv(outfilepath2)
    inchar1 = pd.read_csv(infilepath1)
    inchar2 = pd.read_csv(infilepath2)

    area_1_total = float(inchar1[inchar1["name"] == "basin_area_total"]["value"])
    area_2_total = float(inchar2[inchar2["name"] == "basin_area_total"]["value"])
    total_area = area_1_total + area_2_total

    copy_columns = csv1[
        ["Date", "temperature (celsius)", "precipitation (mm/day)", "flow_observed (mm/day)", "pet (mm/day)",
         "precip_minus_pet (mm/day)"]]

    new_df = copy_columns.copy()
    columns = csv1.columns.tolist()
    columns = columns[5:]
    columns.remove("precip_minus_pet (mm/day)")

    area_1 = area_1_total / total_area
    area_2 = area_2_total / total_area

    for variable in columns:
        new_df["{}".format(variable)] = (csv1["{}".format(variable)] * area_1) + (csv2["{}".format(variable)] * area_2)

    return new_df

def write_out_csv(df, outpath):
    df.to_csv(outpath + "\\output.csv", float_format="%.16f")


if __name__ == "__main__":
    csv1 = r'C:\Users\aheadman\Desktop\JumpDriveStuff\MillCk\output\output.csv'
    csv2 = r'C:\Users\aheadman\Desktop\JumpDriveStuff\MillCk_K\output\output.csv'
    inchar1 = r'C:\Users\aheadman\Desktop\JumpDriveStuff\MillCk\input\characteristics_basin_millCK.csv'
    inchar2 = r'C:\Users\aheadman\Desktop\JumpDriveStuff\MillCk_K\input\K_characteristics_basin_millCK.csv'
    outpath =  r'C:\Users\aheadman\Desktop\JumpDriveStuff\MillCk'

    frame = aggregate(csv1, csv2, inchar1, inchar2)
    write_out_csv(frame, outpath)