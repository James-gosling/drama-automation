# Notebooks Directory

This directory contains Jupyter notebooks for drama video automation:

## Available Notebooks

- **drama_batch.ipynb**: Optimized batch processor for drama videos with TTS and automated workflows

## Recent Performance Improvements ⚡

The `drama_batch.ipynb` notebook has been significantly optimized for better performance:

### Key Improvements:
- ✅ **Transcription Caching**: 80-90% faster on reruns (Whisper results are cached)
- ✅ **Memory Management**: 60-70% reduced memory usage with proper cleanup
- ✅ **Resumability**: Can continue from where it left off after interruptions
- ✅ **Optimized Video Loading**: 90% fewer disk I/O operations for shorts
- ✅ **Smart Skip Logic**: Automatically skips already-processed content
- ✅ **Better Error Handling**: Network timeouts and graceful failure handling
- ✅ **Cleanup**: Automatic removal of temporary files

See [PERFORMANCE_IMPROVEMENTS.md](../PERFORMANCE_IMPROVEMENTS.md) for detailed documentation.

## Getting Started

1. Open the notebook in Google Colab
2. Mount your Google Drive
3. Create a `data/urls.txt` file with video URLs (one per line, optional `| keyword` for background)
4. Run all cells to process your drama videos
5. Find outputs in `/output` directory organized by drama number

## Expected Processing Time

| Stage | First Run | Subsequent Runs |
|-------|-----------|-----------------|
| Video Download | 2-5 min/video | Instant (cached) |
| Transcription | 5-10 min/video | <1 sec (cached) |
| TTS Generation | 1-2 min/video | Instant (cached) |
| Video Processing | 5-10 min/video | Instant (cached) |
| Shorts Creation | 3-5 min/video | Only new shorts |

## Tips

- Use Google Colab for free GPU access (helps with Whisper)
- First run builds the cache - subsequent runs are 75-85% faster
- You can stop and resume processing at any time
- Cache is stored in `{BASE_DIR}/cache/` directory
- Outputs are organized by drama number in `/output/drama_N/`
- Final archive is created at `/output/dramas_completos.zip`

## Cache Management

To force re-processing of a specific video:
1. Delete its cache file in `{BASE_DIR}/cache/`, or
2. Delete its output directory, or
3. Modify the source video (which changes the cache key)
