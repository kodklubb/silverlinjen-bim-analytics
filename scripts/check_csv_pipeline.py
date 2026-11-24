from core.config.settings import MODEL_DIR

from core.pipeline import process_revit_csv


def main():

    df = process_revit_csv(MODEL_DIR)

    structural = df.loc[df["is_structural"]].copy()

    print("\nDataset shape:", df.shape)

    print("\nDataset columns:")
    print(df.columns.tolist())

    print("\nStructural dataset:")

    print(
        structural[[
            "category",
            "material",
            "volume_m3",
            "count"
        ]].head(10).to_string(index=False)
    )

    summary = structural.groupby("category").agg(
        element_count=("count", "sum"),
        total_volume_m3=("volume_m3", "sum")
    )

    print("\nQuantity summary:")
    print(summary.round(3))

    print("\nTotal rows:", len(df))

    print("Structural rows:", len(structural))

    print(
        "Total structural elements:",
        structural["count"].sum()
    )

    print(
        "Missing volumes:",
        structural["volume_m3"].isna().sum()
    )

    print(
        "Missing materials:",
        structural["material"].isna().sum()
    )

    print(
        "Total volume:",
        round(structural["volume_m3"].sum(), 3),
        "m³"
    )

    print("\nRevit CSV pipeline completed successfully!")


if __name__ == "__main__":
    main()