# pylint: disable-all
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numba import njit
# from scipy import stats as ss
from tqdm import tqdm

# |%%--%%| <V5X42kYDU8|pMC68Rd7YR>
filepath = "https://raw.githubusercontent.com/data-8/textbook/main/assets/data/san_francisco_2019.csv"  # noqa

sf2019 = pd.read_csv(filepath)

# |%%--%%| <pMC68Rd7YR|HFfVzFGInu>

sf2019

# |%%--%%| <HFfVzFGInu|RkKnuDJxMc>

sf2019.query("Job == 'Mayor'")

# |%%--%%| <RkKnuDJxMc|YHc6fQAlGY>

sf2019.sort_values("Total Compensation")

# |%%--%%| <YHc6fQAlGY|IhKIrwjjMS>

sf2019 = sf2019.query("Salary > 15000")
sf2019

# |%%--%%| <IhKIrwjjMS|uZ22hTTZSP>

sf_bins = np.arange(0, 726000, 25000)
sf2019[["Total Compensation"]].hist(bins=sf_bins)

# |%%--%%| <uZ22hTTZSP|5eBhE9advh>

sf2019.sort_values("Total Compensation", ascending=False).head(2)

# |%%--%%| <5eBhE9advh|W9vRoUTpiv>

pop_median = np.percentile(sf2019["Total Compensation"], 50)
pop_median

# |%%--%%| <W9vRoUTpiv|aQBIkqCcgx>

our_sample = sf2019.sample(500, replace=False)
our_sample


# |%%--%%| <aQBIkqCcgx|eEd5KO4IZY>

our_sample[["Total Compensation"]].hist(bins=sf_bins)

# |%%--%%| <eEd5KO4IZY|l6TvZJykhN>

est_median = np.percentile(our_sample["Total Compensation"], 50)
est_median

# |%%--%%| <l6TvZJykhN|hhmeefQR8l>

resample1 = our_sample.sample(frac=1, replace=True)

# |%%--%%| <hhmeefQR8l|gPFiJGBjGH>

resample1[["Total Compensation"]].hist(bins=sf_bins)

# |%%--%%| <gPFiJGBjGH|W6PFs9HpxR>

resampled_median_1 = np.percentile(resample1["Total Compensation"], 50)
resampled_median_1

# |%%--%%| <W6PFs9HpxR|jwAdUwCGGE>

resample2 = our_sample.sample(frac=1, replace=True)
resampled_median_2 = np.percentile(resample2["Total Compensation"], 50)
resampled_median_2

# |%%--%%| <jwAdUwCGGE|CXmE1KnPbz>


def one_bootstrap_median():
    resampled_table = our_sample.sample(frac=1, replace=True)
    bootstrapped_median = np.percentile(resampled_table["Total Compensation"], 50)
    return bootstrapped_median


# |%%--%%| <CXmE1KnPbz|BtAdNUaPwh>

one_bootstrap_median()

# |%%--%%| <BtAdNUaPwh|ysS08KOH5Q>

num_repetitions = 5000
bstrap_medians = []
for i in np.arange(num_repetitions):
    bstrap_medians.append(one_bootstrap_median())

# |%%--%%| <ysS08KOH5Q|Xb00Wz4JgM>

plt.hist(bstrap_medians)
plt.axvline(x=pop_median, color="r", label="pop median")
plt.legend()

# |%%--%%| <Xb00Wz4JgM|4SYN4Z0tLk>

left = np.percentile(bstrap_medians, 2.5)
left

# |%%--%%| <4SYN4Z0tLk|fpYyoHcCyz>

right = np.percentile(bstrap_medians, 97.5)
right

# |%%--%%| <fpYyoHcCyz|f3n3KxBbe6>

plt.hist(bstrap_medians)
plt.axvline(x=pop_median, color="r", label="pop median")
plt.axvline(x=left, color="y")
plt.axvline(x=right, color="y")
plt.legend()

# |%%--%%| <f3n3KxBbe6|0rvDuJLO33>


def bootstrap_median(original_sample, num_repetitions: int) -> float:
    medians = np.zeros(num_repetitions)
    for i in np.arange(num_repetitions):
        new_bstrap_sample = original_sample.sample(frac=1, replace=True)
        new_bstrap_median = np.percentile(new_bstrap_sample["Total Compensation"], 50)
        medians[i] = new_bstrap_median
    return medians


# |%%--%%| <0rvDuJLO33|eoME8demfZ>
# THE BIG SIMULATION: This one takes several minutes.

# Generate 100 intervals and put the endpoints in the table intervals

left_ends = np.zeros(100)
right_ends = np.zeros(100)
original_sample = sf2019.sample(500, replace=False)


def simulation(left_ends, right_ends):
    for i in np.arange(100):
        medians = bootstrap_median(original_sample, 5000)
        left_ends[i] = np.percentile(medians, 2.5)
        right_ends[i] = np.percentile(medians, 97.5)


simulation(left_ends, right_ends)
intervals = pd.DataFrame({"Left": left_ends, "Right": right_ends})

# |%%--%%| <eoME8demfZ|30Xj6v17cI>
intervals

# |%%--%%| <30Xj6v17cI|Naa6LivvkR>

pop_median

# |%%--%%| <Naa6LivvkR|ZQNfJzcQ9C>

inside_interval = intervals.query("Left < @pop_median and Right > @pop_median")
inside_interval

# |%%--%%| <ZQNfJzcQ9C|gJOMoDRV2t>
