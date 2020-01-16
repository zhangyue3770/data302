# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

MAP_2020 = {
    # 2020.1 DISTRO
    'distro/core/qiime2-2020.1-py36-osx-conda.yml':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2020.1/release/qiime2-2020.1-py36-osx-conda.yml',
    'distro/core/qiime2-2020.1-py36-linux-conda.yml':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2020.1/release/qiime2-2020.1-py36-linux-conda.yml',
    'distro/core/2020.1':
        'https://google.com',
    'distro/core/qiime20201-BUILDID.zip':
        'https://google.com',

    # 2020.1
    '2020.1/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2020.1/common/gg-13-8-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/common/gg-13-8-99-nb-classifier.qza',
    '2020.1/common/silva-132-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/common/silva-132-99-515-806-nb-classifier.qza',
    '2020.1/common/silva-132-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/common/silva-132-99-nb-classifier.qza',
    '2020.1/common/sepp-refs-gg-13-8.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/common/sepp-refs-gg-13-8.qza',
    '2020.1/common/sepp-refs-silva-128.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/common/sepp-refs-silva-128.qza',
    '2020.1/tutorials/atacama-soils/10p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/atacama-soils/10p/barcodes.fastq.gz',
    '2020.1/tutorials/atacama-soils/10p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/atacama-soils/10p/forward.fastq.gz',
    '2020.1/tutorials/atacama-soils/10p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/atacama-soils/10p/reverse.fastq.gz',
    '2020.1/tutorials/atacama-soils/1p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/atacama-soils/1p/barcodes.fastq.gz',
    '2020.1/tutorials/atacama-soils/1p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/atacama-soils/1p/forward.fastq.gz',
    '2020.1/tutorials/atacama-soils/1p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/atacama-soils/1p/reverse.fastq.gz',
    '2020.1/tutorials/chimera/atacama-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/chimera/atacama-table.qza',
    '2020.1/tutorials/chimera/atacama-rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/chimera/atacama-rep-seqs.qza',
    '2020.1/tutorials/exporting/feature-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/exporting/feature-table.qza',
    '2020.1/tutorials/exporting/unrooted-tree.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/exporting/unrooted-tree.qza',
    '2020.1/tutorials/filtering/distance-matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/filtering/distance-matrix.qza',
    '2020.1/tutorials/filtering/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/filtering/table.qza',
    '2020.1/tutorials/filtering/taxonomy.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/filtering/taxonomy.qza',
    '2020.1/tutorials/filtering/sequences.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/filtering/sequences.qza',
    '2020.1/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2020.1/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2020.1/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2020.1/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2020.1/tutorials/fmt-cdiff-khanna/manifest.csv':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2020.1/tutorials/fmt-cdiff-khanna/manifest.csv',
    '2020.1/tutorials/fmt-cdiff-khanna/sequence_files.zip':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2020.1/tutorials/fmt-cdiff-khanna/sequence_files.zip',
    '2020.1/tutorials/gneiss/sample-metadata.tsv':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/gneiss/sample-metadata.tsv',
    '2020.1/tutorials/gneiss/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/gneiss/table.qza',
    '2020.1/tutorials/gneiss/taxa.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/gneiss/taxa.qza',
    '2020.1/tutorials/importing/aligned-sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/aligned-sequences.fna',
    '2020.1/tutorials/importing/casava-18-paired-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/casava-18-paired-end-demultiplexed.zip',
    '2020.1/tutorials/importing/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/casava-18-single-end-demultiplexed.zip',
    '2020.1/tutorials/importing/feature-table-v100.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/feature-table-v100.biom',
    '2020.1/tutorials/importing/feature-table-v210.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/feature-table-v210.biom',
    '2020.1/tutorials/importing/pe-64-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/pe-64-manifest',
    '2020.1/tutorials/importing/pe-64.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/pe-64.zip',
    '2020.1/tutorials/importing/se-33-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/se-33-manifest',
    '2020.1/tutorials/importing/se-33.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/se-33.zip',
    '2020.1/tutorials/importing/sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/sequences.fna',
    '2020.1/tutorials/importing/unrooted-tree.tre':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/importing/unrooted-tree.tre',
    '2020.1/tutorials/longitudinal/ecam_table_taxa.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/longitudinal/ecam_table_taxa.qza',
    '2020.1/tutorials/longitudinal/ecam_shannon.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/longitudinal/ecam_shannon.qza',
    '2020.1/tutorials/longitudinal/unweighted_unifrac_distance_matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/longitudinal/unweighted_unifrac_distance_matrix.qza',
    '2020.1/tutorials/longitudinal/ecam_table_maturity.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/longitudinal/ecam_table_maturity.qza',
    '2020.1/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz',
    '2020.1/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz',
    '2020.1/tutorials/metadata/faith_pd_vector.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/metadata/faith_pd_vector.qza',
    '2020.1/tutorials/metadata/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/metadata/rep-seqs.qza',
    '2020.1/tutorials/metadata/taxonomy.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/metadata/taxonomy.qza',
    '2020.1/tutorials/metadata/unweighted_unifrac_pcoa_results.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/metadata/unweighted_unifrac_pcoa_results.qza',
    '2020.1/tutorials/otu-clustering/seqs.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/otu-clustering/seqs.fna',
    '2020.1/tutorials/otu-clustering/85_otus.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/otu-clustering/85_otus.qza',
    '2020.1/tutorials/pd-mice/animal_distal_gut.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2020.1/tutorials/pd-mice/animal_distal_gut.qza',
    '2020.1/tutorials/pd-mice/demultiplexed_seqs.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/pd-mice/demultiplexed_seqs.zip',
    '2020.1/tutorials/pd-mice/manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/pd-mice/manifest',
    '2020.1/tutorials/pd-mice/ref_seqs_v4.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2020.1/tutorials/pd-mice/ref_seqs_v4.qza',
    '2020.1/tutorials/pd-mice/ref_tax.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2020.1/tutorials/pd-mice/ref_tax.qza',
    '2020.1/tutorials/quality-control/qc-mock-3-expected.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/quality-control/qc-mock-3-expected.qza',
    '2020.1/tutorials/quality-control/qc-mock-3-observed.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/quality-control/qc-mock-3-observed.qza',
    '2020.1/tutorials/quality-control/query-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/quality-control/query-seqs.qza',
    '2020.1/tutorials/quality-control/reference-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/quality-control/reference-seqs.qza',
    '2020.1/tutorials/quality-control/query-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/quality-control/query-table.qza',
    '2020.1/tutorials/read-joining/atacama-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/read-joining/atacama-seqs.qza',
    '2020.1/tutorials/read-joining/fj-joined.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/read-joining/fj-joined.zip',
    '2020.1/tutorials/sample-classifier/atacama-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/sample-classifier/atacama-table.qza',
    '2020.1/tutorials/sample-classifier/moving-pictures-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/sample-classifier/moving-pictures-table.qza',
    '2020.1/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2020.1/tutorials/training-feature-classifiers/85_otus.fasta':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/training-feature-classifiers/85_otus.fasta',
    '2020.1/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2020.1/tutorials/training-feature-classifiers/rep-seqs.qza',
    '2020.1/tutorials/phylogeny/rep-seqs.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2020.1/tutorials/phylogeny/rep-seqs.qza',

    # Sample Metadata (hosted on Google Sheets)

    ## FMT
    '2020.1/tutorials/fmt/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1TSFsvAo0aIHnNy-67PlAjXhhGQx6VtXCEzSmV9KeVbc/edit?usp=sharing',
    '2020.1/tutorials/fmt/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1TSFsvAo0aIHnNy-67PlAjXhhGQx6VtXCEzSmV9KeVbc/export?gid=0&format=tsv',

    ## Moving Pictures
    '2020.1/tutorials/moving-pictures/sample_metadata':
        'https://docs.google.com/spreadsheets/d/15HpBuwlUbm6Yg12qOtKOrr2dUM7B2ityv9te7KB7Xq8/edit?usp=sharing',
    '2020.1/tutorials/moving-pictures/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/15HpBuwlUbm6Yg12qOtKOrr2dUM7B2ityv9te7KB7Xq8/export?gid=0&format=tsv',

    ## Atacama
    '2020.1/tutorials/atacama-soils/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1AFtHGlLIHy4-hwAyAL0EQUMLvZtONK5bgZ0JSInSRYc/edit?usp=sharing',
    '2020.1/tutorials/atacama-soils/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1AFtHGlLIHy4-hwAyAL0EQUMLvZtONK5bgZ0JSInSRYc/export?gid=0&format=tsv',

    ## The following tutorials are the "weird" ones, they use the *new* docs sharing menu, via "File -> Publish to the Web" dialog for TSV export.

    ## Longitudinal
    '2020.1/tutorials/longitudinal/sample_metadata':
        'https://docs.google.com/spreadsheets/d/19AZnLnTRUG4jz8ICPu4cPhNva3dipvnUXtqCSfZIiyg/edit?usp=sharing',
    '2020.1/tutorials/longitudinal/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ68O0P1syi1au1G4u-guxaNNAbUnvCmQYYmEKvWDGt_all3c1HPJ_2j9abEW6bI9YifZcXLlvy5joh/pub?gid=1303657428&single=true&output=tsv',

    ## FMT Cdiff
    '2020.1/tutorials/fmt-cdiff-khanna/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1pR29THjgcNMMMCBwwAbfZDD5hHhjNzocBL0V7oroY2g/edit?usp=sharing',
    '2020.1/tutorials/fmt-cdiff-khanna/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vQEytlplv_yNjq_d_mTA9Xw-ATgmGqodvau4moKm3q3qCwlmbvjOW9jeO3rdxi7SMEaK8-nZMeF1BSS/pub?gid=283132897&single=true&output=tsv',

    ## PD Mice
    '2020.1/tutorials/pd-mice/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1EIjwTSWoBjm3HAjuM0oo5VLA6whVxS6YCzVOJE2y3eU/edit?usp=sharing',
    '2020.1/tutorials/pd-mice/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vTUKT61yWMqo0xLFST1cYnIUKOvDm5YMk7i1h-MiJHU84cWkQ8ehvR3xPATMD21ZGkguNiywN98JWG5/pub?gid=1509704122&single=true&output=tsv',
}
