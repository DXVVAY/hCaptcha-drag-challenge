# hCaptcha image_drag_drop solver
<div style="text-align: center;">
  <img src="https://dexv.site/content/cdn/gLzcKUDypDGr.png" alt="image" width="1500">
</div>
made by Dexv! 
https://t.me/dexv0

> [!CAUTION]
> This challenge is probs just a PoC and they might remove it!
> Average solve time is around 0.5-0.8 s :D

## Usage

Local:
```python
from solver import DragDrop

# hCaptchas getcaptcha endpoint response
captcha = {
    "request_type": "image_drag_drop",
    "tasklist": [
        {
            "datapoint_uri": "https://imgs3.hcaptcha.com/tip/400a24ee2e38feb55bbf2cb251d5b0127fb6c114a596e4d7a5112459f4448469/ece8b9a29ccb58a7a6546b13dce88d2fdb5e5f7f0a12e762dad4bd332377f734.png",
            "task_key": "3b9622ff-83eb-435b-8c97-f430c7c7ad8e",
            "entities": [
                {
                    "entity_id": "51b2ad74-bb2b-40c4-9793-cd08df1ac29b",
                    "entity_uri": "https://imgs3.hcaptcha.com/tip/3f0adfa72a18454ad2e1da7b6ed48dca6d9e4f02307765598443b622bc1244e6/872424df274307ebf5f188a4d62b04eff42988d812885da7c4785d5ac49180e6.png",
                    "coords": [
                        405,
                        105
                    ],
                    "size": [
                        100,
                        100
                    ],
                    "metadata": {
                        "original_uri": "https://fantasia-assets.hcaptcha.com/d-and-d-completeBGpath-5-auro_2_RE_36EFFA9D/8ac7bb42-dea8-462c-917b-0af31aff40b9_draggable_0.png"
                    }
                },
                {
                    "entity_id": "56f6d89a-7ec4-4bc7-978c-38c8d9d43e00",
                    "entity_uri": "https://imgs3.hcaptcha.com/tip/83af7e40b068c1e3a20334f82682d20dcf8a282020a9d3e8cd2c8198bd7bc361/904dac201d9e60ecf15cc333b4a5827f8bb700dc309f78052748b37fd5f2e94d.png",
                    "coords": [
                        405,
                        215
                    ],
                    "size": [
                        100,
                        100
                    ],
                    "metadata": {
                        "original_uri": "https://fantasia-assets.hcaptcha.com/d-and-d-completeBGpath-5-auro_2_RE_36EFFA9D/13c0129b-588a-4f8d-a3d2-baa094f12e2c_draggable_1.png"
                    }
                }
            ]
        }
    ]
}

inst = DragDrop(captcha, verbose=False)
print(inst.solve())
```

API:
```cmd
uvicorn api:app --port 4200
```

```python
import requests

data = {
    "captcha": {
        "request_type": "",
        "tasklist": []
    }
}

result = requests.post("http://127.0.0.1:4200/solve", json=data).json()
print(result.get("result", "Failed"))
```

# Credits

* **DEXV** - *Shit head (retarded)* - [DEXV](https://dexv.lol) - Main Author
* **DCH** - *Frenchie* - [DCH](https://t.me/azulax1) - Idea of using opencv
