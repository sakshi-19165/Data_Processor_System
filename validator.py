def validate_data(df):
    errors = []

    if "email" in df.columns:
        invalid_emails = df[~df["email"].astype(str).str.contains("@")]
        if not invalid_emails.empty:
            errors.append("Invalid email addresses found")

    if "age" in df.columns:
        if (df["age"] < 0).any():
            errors.append("Negative age values found")

    return errors
