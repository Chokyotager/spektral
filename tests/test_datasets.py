from spektral.data import DisjointLoader, BatchLoader
from spektral.datasets import qm9, citation, graphsage, mnist, tudataset

batch_size = 3


def test_citation():
    dataset = citation.Cora()
    dataset = citation.Citeseer(random_split=True)
    dataset = citation.Pubmed(normalize_x=True)


def test_graphsage():
    # Test only PPI because Travis otherwise runs into memory errors
    dataset = graphsage.PPI()


def test_mnist():
    mnist.load_data(k=8, noise_level=0.1)


def test_qm9():
    dataset = qm9.QM9(amount=100)
    dl = DisjointLoader(dataset, batch_size=batch_size)
    dl.__next__()

    bl = BatchLoader(dataset, batch_size=batch_size)
    bl.__next__()


def test_tud():
    # Edge labels + edge attributes
    dataset = tudataset.TUDataset('BZR_MD', clean=False)
    dl = DisjointLoader(dataset, batch_size=batch_size)
    dl.__next__()

    bl = BatchLoader(dataset, batch_size=batch_size)
    bl.__next__()

    # Node labels + node attributes + clean version
    dataset = tudataset.TUDataset('ENZYMES', clean=True)
    dl = DisjointLoader(dataset, batch_size=batch_size)
    dl.__next__()

    bl = BatchLoader(dataset, batch_size=batch_size)
    bl.__next__()
