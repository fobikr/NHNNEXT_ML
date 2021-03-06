#elice_3_31_solution.py
import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster
import numpy as np
import pandas as pd
import elice_utils

def main():
    champs_df = pd.read_pickle('champ_df.pd')
    # 1
    champ_pca_array = run_PCA(champs_df, 2)

    champ_classes = run_kmeans(champ_pca_array, 4 , [0,  40,80, 120])

    # 4
    print(elice_utils.plot_champions(champs_df, champ_pca_array, champ_classes))

    # 5
    print(get_champs_by_cluster(champs_df, champ_classes, 3))

def run_kmeans(champ_pca_array, num_clusters, initial_centroid_indices):
    # Implement K-Means algorithm using sklearn.cluster.KMeans.
    array = np.array(champ_pca_array)
    
    classifier = sklearn.cluster.KMeans( num_clusters, array[initial_centroid_indices], n_init = 1)
    classifier.fit(array)
    # 2

    # 3
    return classifier.labels_

def run_PCA(champs_df, num_components):
    # Normalize Attributes
    scaler = sklearn.preprocessing.MinMaxScaler()
    for attr in champs_df:
        champs_df[attr] = scaler.fit_transform(np.array(champs_df[attr]).astype('float64'))

    # Run PCA
    pca = sklearn.decomposition.PCA(n_components = num_components)
    pca.fit(champs_df)
    champ_pca_array = pca.transform(champs_df)

    return champ_pca_array

def get_champs_by_cluster(champs_df, champ_classes, cluster_idx):
    return champs_df.index[champ_classes == cluster_idx].values

if __name__ == '__main__':
    main()