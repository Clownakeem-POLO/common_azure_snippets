# Calculate the correlation matrix on the cleaned dataframe
correlation_matrix = new_mgh.corr()
correlation_matrix

# Plot it so the relationships are easy to read
plt.figure(figsize=(15, 15))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".4f")
plt.show()
