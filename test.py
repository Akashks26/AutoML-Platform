from ml_engine.predict import predict

input_data = {
    "age"         : 34,
    "salary"      : 55000,
    "experience"  : 6,
    "credit_score": 720
}

result = predict(input_data)

print("\n" + "=" * 40)
print("       LOAN PREDICTION RESULT")
print("=" * 40)

if "error" in result:
    print(f"\n  Error: {result['error']}")

else:
    print(f"\n  Decision    : {result['Decision']}")
    print(f"  Confidence  : {result['Confidence']}")

    print("\n  Key Factors:")
    for factor in result["Key Factors"]:
        print(f"    - {factor}")

    print("\n  Applicant Profile:")
    for field, value in result["Input Summary"].items():
        print(f"    {field:<15}: {value}")

print("\n" + "=" * 40 + "\n")