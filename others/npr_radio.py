

for mileage in range(1_000_000):
    mileage_str = str(mileage)

    last_four = mileage_str[-4:]
    last_five = mileage_str[-5:]

    if (last_four == last_four[::-1]) and (last_five != last_five[::-1]):
        mileage_str = str(mileage +1)
        last_five = mileage_str[-5:]

        if (last_five == last_five[::-1]):
            mileage_str = str(mileage + 2)
            mid_four = mileage_str[1:5]

            if (mid_four == mid_four[::-1]):
                mileage_str = str(mileage + 3)

                if (mileage_str == mileage_str[::-1]):
                    print(f"the mile is = {mileage}")

