# Search Engine for Vietnamese Law Documents

## Overview

This project implements a search engine for Vietnamese legal documents with a complete end-to-end pipeline, from data collection to retrieval comparison. The main focus of the project is to compare different information retrieval approaches applied to Vietnamese law texts, specifically dense retrieval methods and sparse retrieval methods using BM25. The system is designed for experimental and research purposes rather than production deployment.

## Project Objectives

- Crawl Vietnamese legal documents from online sources
- Preprocess and normalize raw legal text
- Build retrieval methods for document search
- Compare retrieval results between dense and sparse approaches
- Analyze the strengths and weaknesses of each method

## Methodology

### 1. Data Crawling

Legal documents are collected from Vietnamese law sources using custom crawling scripts. The crawled data is stored in JSON format for further processing.

### 2. Preprocessing

The preprocessing stage includes text cleaning, normalization, and chunking long documents into smaller segments suitable for retrieval. This ensures that the data is in an optimal format for both sparse and dense retrieval methods.

### 3. Retrieval Methods

Two retrieval approaches are implemented in this project:

**Sparse Retrieval with BM25**

A traditional keyword-based method using term frequency and inverse document frequency. This approach relies on exact term matching and statistical measures to rank documents.

**Dense Retrieval**

An embedding-based approach that retrieves documents based on semantic similarity. This method uses neural networks to encode documents and queries into dense vector representations.

These approaches are treated as retrieval methods rather than fixed models, allowing for flexible experimentation and comparison.

### 4. Retrieval and Comparison

The main.py script loads processed data, executes both retrieval methods on the same set of queries, and collects and compares retrieval results. This allows for direct performance comparison between the two approaches.

## How to Run

To run the retrieval experiments and comparisons, navigate to the search_engine_model directory and execute the main script:

```bash
cd search_engine_model
python main.py
```

The main.py file serves as the single entry point for running retrieval experiments and comparisons.

## Notes

- Large datasets are not intended to be versioned directly in Git
- Data files can be regenerated using the provided crawling and preprocessing notebooks
- The project is designed for experimentation, analysis, and learning purposes
- All code and documentation are structured to facilitate understanding of information retrieval concepts applied to Vietnamese legal texts

## Possible Extensions

- Hybrid retrieval combining BM25 and dense methods
- Reranking models to improve top-k results
- Evaluation metrics including Recall@K, MRR, and nDCG
- API or web-based demo interface for interactive searching
- Support for additional Vietnamese legal document sources
- Query expansion and refinement techniques

