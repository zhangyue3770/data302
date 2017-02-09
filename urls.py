# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa


MAP = {
    # DISTRO
    'distro/core/2.0.6':
        'https://s3-us-west-2.amazonaws.com/9400115901699159151932/qiime206-1484941248.zip',

    # 'distro/core/2017.2':
    #     '',

    'distro/core/qiime2-2017.2-conda-osx-64.txt':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/distro/core/qiime2-2017.2-conda-osx-64.txt',

    'distro/core/qiime2-2017.2-conda-linux-64.txt':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/distro/core/qiime2-2017.2-conda-linux-64.txt',

    'distro/core/qiime206.zip':
        'https://s3-us-west-2.amazonaws.com/9400115901699159151932/qiime206-1484941248.zip',

    'distro/core/qiime206-1479486933.zip':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/distro/core/QIIME%202%20Core%20-%202.0.6%20%281479486933%29.zip',

    'distro/core/qiime206-1484941248.zip':
        'https://s3-us-west-2.amazonaws.com/9400115901699159151932/qiime206-1484941248.zip',

    # 2017.2
    '2017.2/common/silva-119-99-nb-classifier.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/common/2017.2/silva-119-99-nb-classifier.qza',

    '2017.2/common/gg-13-8-99-nb-classifier.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/common/2017.2/gg-13-8-99-nb-classifier.qza',

    '2017.2/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/common/2017.2/gg-13-8-99-515-806-nb-classifier.qza',

    '2017.2/common/silva-119-99-515-806-nb-classifier.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/common/2017.2/silva-119-99-515-806-nb-classifier.qza',

    '2017.2/tutorials/atacama-soils/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1xMP1EjKZDrzdKLnQr7LGVAY35ongxrreT28k0EACtfg/export?gid=0&format=tsv',

    '2017.2/tutorials/atacama-soils/1p/forward.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/importing-sequence-data/2017.2/emp-paired-end-sequences/atacama-1p/forward.fastq.gz',

    '2017.2/tutorials/atacama-soils/1p/reverse.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/importing-sequence-data/2017.2/emp-paired-end-sequences/atacama-1p/reverse.fastq.gz',

    '2017.2/tutorials/atacama-soils/1p/barcodes.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/importing-sequence-data/2017.2/emp-paired-end-sequences/atacama-1p/barcodes.fastq.gz',

    '2017.2/tutorials/atacama-soils/10p/forward.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/importing-sequence-data/2017.2/emp-paired-end-sequences/atacama-10p/forward.fastq.gz',

    '2017.2/tutorials/atacama-soils/10p/reverse.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/importing-sequence-data/2017.2/emp-paired-end-sequences/atacama-10p/reverse.fastq.gz',

    '2017.2/tutorials/atacama-soils/10p/barcodes.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/importing-sequence-data/2017.2/emp-paired-end-sequences/atacama-10p/barcodes.fastq.gz',

    '2017.2/tutorials/atacama-soils/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1xMP1EjKZDrzdKLnQr7LGVAY35ongxrreT28k0EACtfg/edit?usp=sharing',

    '2017.2/tutorials/training-feature-classifiers/85_otus.fasta':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/training-feature-classifiers/2017.2/85_otus.fasta',

    '2017.2/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/training-feature-classifiers/2017.2/85_otu_taxonomy.txt',

    '2017.2/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/training-feature-classifiers/2017.2/rep-seqs.qza',

    '2017.2/tutorials/filtering/table.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/filtering/2017.2/table.qza',

    '2017.2/tutorials/filtering/distance-matrix.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/filtering/2017.2/distance-matrix.qza',

    '2017.2/tutorials/fmt/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/197f9kTKhcvcwqIjQaSkDHqsWeLO5jNN2_LlAN3NuadI/export?gid=0&format=tsv',

    '2017.2/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2017.2/fmt-tutorial-demux-1-10p.qza',

    '2017.2/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2017.2/fmt-tutorial-demux-2-10p.qza',

    '2017.2/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2017.2/fmt-tutorial-demux-1-1p.qza',

    '2017.2/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2017.2/fmt-tutorial-demux-2-1p.qza',

    '2017.2/tutorials/fmt/sample_metadata':
        'https://docs.google.com/spreadsheets/d/197f9kTKhcvcwqIjQaSkDHqsWeLO5jNN2_LlAN3NuadI/edit?usp=sharing',

    '2017.2/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-moving-pictures-tutorial/2017.2/emp-single-end-sequences/barcodes.fastq.gz',

    '2017.2/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-moving-pictures-tutorial/2017.2/emp-single-end-sequences/sequences.fastq.gz',

    '2017.2/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/importing-sequence-data/2017.2/casava-18-single-end-demultiplexed.zip',

    '2017.2/tutorials/importing-sequence-data/casava-18-paired-end-demultiplexed.zip':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/importing-sequence-data/2017.2/casava-18-paired-end-demultiplexed.zip',

    '2017.2/tutorials/importing-sequence-data/feature-table-v100.biom':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/examples/2017.2/feature-table-v100.biom',

    '2017.2/tutorials/importing-sequence-data/feature-table-v210.biom':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/examples/2017.2/feature-table-v210.biom',

    '2017.2/tutorials/moving-pictures/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1WwCnhP7VbiVXY5-XHLoYAT-wAU68ItEF117TYJeQCrg/export?gid=0&format=tsv',

    '2017.2/tutorials/moving-pictures/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1WwCnhP7VbiVXY5-XHLoYAT-wAU68ItEF117TYJeQCrg/edit?usp=sharing',

    # 2.0.6
    '2.0.6/tutorials/examples/feature-table.biom':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/examples/2.0.6/feature-table.biom',

    '2.0.6/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.6/fmt-tutorial-demux-1-1p.qza',

    '2.0.6/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.6/fmt-tutorial-demux-2-1p.qza',

    '2.0.6/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.6/fmt-tutorial-demux-1-10p.qza',

    '2.0.6/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.6/fmt-tutorial-demux-2-10p.qza',

    '2.0.6/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/common/2.0.6/gg-13-8-99-515-806-nb-classifier.qza',

    '2.0.6/tutorials/fmt/fmt-tutorial-demux-1-full.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.6/fmt-tutorial-demux-1-full.qza',

    '2.0.6/tutorials/fmt/fmt-tutorial-demux-2-full.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.6/fmt-tutorial-demux-2-full.qza',

    '2.0.6/tutorials/filtering-feature-tables/table.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/filtering-feature-tables/table.qza',

    '2.0.6/common/silva-119-99-515-806-nb-classifier.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/common/2.0.6/silva-119-99-515-806-nb-classifier.qza',

    '2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.6/fmt-tutorial-raw-sequences-1.qza',

    '2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.6/fmt-tutorial-raw-sequences-2.qza',

    '2.0.6/common/gg-13-8-99-full-length-nb-classifier.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/common/2.0.6/gg-13-8-99-full-length-nb-classifier.qza',

    '2.0.6/tutorials/88soils/88soils-tutorial-demux-1p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-88soils-tutorial/2.0.6/88soils-tutorial-demux-1p.qza',

    '2.0.6/tutorials/88soils/88soils-tutorial-demux-10p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-88soils-tutorial/2.0.6/88soils-tutorial-demux-10p.qza',

    '2.0.6/common/silva-119-99-full-length-nb-classifier.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/common/2.0.6/silva-119-99-full-length-nb-classifier.qza',

    '2.0.6/tutorials/88soils/88soils-tutorial-demux-full.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-88soils-tutorial/2.0.6/88soils-tutorial-demux-full.qza',

    '2.0.6/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/training-feature-classifiers/2.0.6/rep-seqs.qza',

    '2.0.6/tutorials/88soils/88soils-tutorial-raw-sequences.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-88soils-tutorial/2.0.6/88soils-tutorial-raw-sequences.qza',

    '2.0.6/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-moving-pictures-tutorial/2.0.6/raw-sequences/barcodes.fastq.gz',

    '2.0.6/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-moving-pictures-tutorial/2.0.6/raw-sequences/sequences.fastq.gz',

    '2.0.6/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/training-feature-classifiers/2.0.6/85_otu_taxonomy.txt',

    '2.0.6/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/importing-sequence-data/2.0.6/casava-18-single-end-demultiplexed.zip',

    '2.0.6/tutorials/training-feature-classifiers/aligned_85_otu_sequences.fasta.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/training-feature-classifiers/2.0.6/aligned_85_otu_sequences.fasta.gz',

    # 2.0.5
    '2.0.5/tutorials/examples/feature-table.biom':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/examples/2.0.5/feature-table.biom',

    '2.0.5/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.5/fmt-tutorial-demux-1-1p.qza',

    '2.0.5/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.5/fmt-tutorial-demux-2-1p.qza',

    '2.0.5/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.5/fmt-tutorial-demux-1-10p.qza',

    '2.0.5/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.5/fmt-tutorial-demux-2-10p.qza',

    '2.0.5/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/common/2.0.5/gg-13-8-99-515-806-nb-classifier.qza',

    '2.0.5/tutorials/fmt/fmt-tutorial-demux-1-full.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.5/fmt-tutorial-demux-1-full.qza',

    '2.0.5/tutorials/fmt/fmt-tutorial-demux-2-full.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.5/fmt-tutorial-demux-2-full.qza',

    '2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.5/fmt-tutorial-raw-sequences-1.qza',

    '2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-fmt-tutorial/2.0.5/fmt-tutorial-raw-sequences-2.qza',

    '2.0.5/tutorials/88soils/88soils-tutorial-demux-1p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-88soils-tutorial/2.0.5/88soils-tutorial-demux-1p.qza',

    '2.0.5/tutorials/88soils/88soils-tutorial-demux-10p.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-88soils-tutorial/2.0.5/88soils-tutorial-demux-10p.qza',

    '2.0.5/tutorials/88soils/88soils-tutorial-demux-full.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-88soils-tutorial/2.0.5/88soils-tutorial-demux-full.qza',

    '2.0.5/tutorials/88soils/88soils-tutorial-raw-sequences.qza':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-88soils-tutorial/2.0.5/88soils-tutorial-raw-sequences.qza',

    '2.0.5/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-moving-pictures-tutorial/2.0.5/raw-sequences/barcodes.fastq.gz',

    '2.0.5/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz':
        'https://dl.dropboxusercontent.com/u/2868868/data/qiime2/tutorials/2016-moving-pictures-tutorial/2.0.5/raw-sequences/sequences.fastq.gz',

}
