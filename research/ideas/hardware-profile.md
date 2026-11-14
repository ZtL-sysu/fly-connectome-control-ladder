# Hardware and execution envelope

Local measured: macOS ARM64, 8 CPU cores, 16GiB RAM, Python 3.11.15 in project Conda ceg_snn_mi, Torch 2.13.0, MPS available; dense float32 matmul smoke matched CPU. The full official flyvis MPS/scatter/dynamics path has not been verified. CPU retained for NumPy/SciPy/source parsing; unsupported MPS operations need explicit fallbacks. Free workspace disk ~43.8GiB at initial probe.

Remote measured in Novix task21782: RTX4090, device0, compute capability8.9, total memory47,661,645,824 bytes (44.388GiB), Python3.11.18, torch2.11.0+cu130, CUDA available. Provider novixlet/resource-pool exp-4090 explicitly requested by user. The generic default pool is not used.

Planning task: single GPU <=30min, <=12 turns, source/hardware audit only; training prohibited. If protocol gates pass, initial pilot allowance is two single-GPU tasks <=2h each. Runtime of full CUDA forward/backward remains unmeasured; published CPU times are evidence only for an initial estimate. No broad tuning/search or unbounded trial queues. Exact seed/run counts will be fixed in the accepted claim contract.

Official source helpers hide CUDA when CUDA_VISIBLE_DEVICES is absent, so execution entry must respect scheduler-assigned visible device and assert tensor/parameter device, not just torch.cuda availability. Native flyvis chooses CPU or CUDA, not MPS by default.
