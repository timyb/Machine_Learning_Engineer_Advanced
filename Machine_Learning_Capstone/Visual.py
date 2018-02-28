def skew_distribution(feature_lst, transformed = False):
	"""
    Visualization code for displaying skewed distributions of features

    """

    # Create figure
    fig = plt.figure((11,5))

    #Skewed feature plotting
    for counter, feature in enumerate(feature_lst):
    	ax = fig.add_subplot(1,2,counter)
    	ax.hist(data[feature], bins = 25, color = '#00A0A0')
        ax.set_title("'%s' Feature Distribution"%(feature), fontsize = 14)
        ax.set_xlabel("Value")
        ax.set_ylabel("Number of Records")
        ax.set_ylim((0, 2000))
        ax.set_yticks([0, 500, 1000, 1500, 2000])
        ax.set_yticklabels([0, 500, 1000, 1500, ">2000"])