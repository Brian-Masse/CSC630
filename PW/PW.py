import matplotlib as plt
import seaborn as sns

dark_purple = (190 / 255, 212 / 255, 255 / 255)
mid_purple = (201 / 255, 193 / 255, 245 / 255)
tan = (252 / 255, 209 / 255, 175 / 255)

plt.rcParams.update({'font.size': 5})
purpleCmap = sns.cubehelix_palette(as_cmap=True)
beachCMap = plt.colors.LinearSegmentedColormap.from_list(
    "", [dark_purple, mid_purple, tan])

deaths = sns.load_dataset("AnimalDeaths")
percentOfGender = deaths.pivot_table(
    "percent", index="Animal", columns="Gender")
percentOfAnimalKills = deaths.pivot_table(
    "percent2", index="Animal", columns="Gender")


# pG = sns.heatmap(percentOfGender, vmin=0, vmax=50, cmap=purpleCmap, annot=True).set(
#     title="Deaths by an animal, as a percent of the total deaths of a gender")
pAK = sns.heatmap(percentOfAnimalKills, vmin=0, vmax=100, cmap=purpleCmap, annot=True).set(
    title="Deaths of a gender by an animal, as a percent of the total kills by that animal")

plt.pyplot.show()
