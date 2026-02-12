#include <cmath>

// daily_rate calculates the daily rate given an hourly rate
double daily_rate(double hourly_rate) {
    return hourly_rate * 8;
}

// apply_discount calculates the price after a discount
double apply_discount(double before_discount, double discount) {
    return before_discount * (1 - discount / 100);
}

// monthly_rate calculates the monthly rate
// The returned monthly rate is rounded up
int monthly_rate(double hourly_rate, double discount) {
    double monthly = daily_rate(hourly_rate) * 22;
    double discounted = apply_discount(monthly, discount);
    return ceil(discounted);
}

// days_in_budget calculates how many full days fit in the budget
// Rounded down
int days_in_budget(int budget, double hourly_rate, double discount) {
    double discounted_daily = apply_discount(daily_rate(hourly_rate), discount);
    return floor(budget / discounted_daily);
}

