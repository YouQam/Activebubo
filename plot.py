import numpy as np
import matplotlib.pyplot as plt
#Defining Function
def boxplot_distance(data_to_plot):#an array of data for each month
        
        data_to_plot = [collectn_1,collectn_2,collectn_3,collectn_4]
        fig = plt.figure(1,figsize=(9,6))
        ax = fig.add_subplot(111)
        bp = ax.boxplot(data_to_plot,0,'',patch_artist='True')

        #changing colours 
        for box in bp['boxes']:
                #outline color
                box.set( color='#7570b3', linewidth=2)
                #fill color
                box.set( facecolor = '#1b9e77')
        #whiskers
        for whisker in bp['whiskers']:
                whisker.set( color ='#7570b3', linewidth =2)

        for cap in bp['caps']:
                cap.set( color ='#7570b3', linewidth =2)

        for median in bp['medians']:
                median.set( color ='#b2df8a', linewidth=2)

        for flier in bp['fliers']:
                flier.set(marker ='o',color = '#e7298a', alpha= 0.5)
        ax.yaxis.grid(True)
        ax.set_title('Activebubo in terms of distance')
        ax.set_xlabel('month')
        ax.set_ylabel('distance')
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        fig.savefig('boxplot1.png',bbox_inches='tight')
        print('done')
        plt.show()