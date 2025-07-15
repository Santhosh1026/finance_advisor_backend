def simulate_score(profile) -> dict:
    score = 300

    # Weights
    weights = {
        "payment_history": 0.35,
        "utilization": 0.30,
        "age": 0.15,
        "inquiries": 0.10,
        "mix": 0.10,
    }

    # Payment History
    on_time = sum(1 for p in profile.payment_history.values() if p == "on_time")
    late = sum(1 for p in profile.payment_history.values() if p == "late")
    total = on_time + late if (on_time + late) > 0 else 1
    payment_score = (on_time / total) * 100
    score += int((payment_score / 100) * weights["payment_history"] * 600)

    # Utilization
    utilization_score = max(0, 1 - profile.utilization)
    score += int(utilization_score * weights["utilization"] * 600)

    # Credit Age
    age_score = min(profile.credit_age_months / 120, 1.0)
    score += int(age_score * weights["age"] * 600)

    # Inquiries
    inquiry_score = max(0, 1 - (profile.inquiries_last_6m / 5))
    score += int(inquiry_score * weights["inquiries"] * 600)

    # Mix
    mix_score = 1 if all(x in profile.account_mix for x in ["loan", "credit card"]) else 0.5
    score += int(mix_score * weights["mix"] * 600)

    return {
        "score": min(score, 900),
        "breakdown": {
            "payment_score": round(payment_score, 2),
            "utilization_score": round(profile.utilization * 100, 2),
            "credit_age": profile.credit_age_months,
            "inquiries": profile.inquiries_last_6m,
            "mix": profile.account_mix,
        }
    }