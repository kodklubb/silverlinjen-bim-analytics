from core.config.settings import IFC_FILE

from core.pipeline import process_ifc


def main():

    df = process_ifc(IFC_FILE)

    structural = df.loc[
        df["is_structural"]
    ].copy()

    print("\nDataset shape:", df.shape)

    print("\nDataset columns:")
    print(df.columns.tolist())

    print("\nStructural dataset:")

    print(
        structural[[
            "category",
            "material",
            "net_volume_m3"
        ]].head(10).to_string(index=False)
    )

    print("\nMaterial distribution:")
    print(
        structural["material"].value_counts(
            dropna=False
        )
    )

    print("\nTotal IFC elements:", len(df))

    print("Structural elements:", len(structural))

    print(
        "Excluded elements:",
        len(df) - len(structural)
    )

    print(
        "Missing materials:",
        structural["material"].isna().sum()
    )

    print(
        "Total volume:",
        round(structural["net_volume_m3"].sum(), 3),
        "m³"
    )

    print("\nIFC pipeline completed successfully!")


if __name__ == "__main__":
    main()