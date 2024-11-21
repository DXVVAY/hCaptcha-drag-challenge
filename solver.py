import base64, requests, numpy, cv2, time
from utils import *

class DragDrop:
    def __init__(self, captcha: dict, verbose: bool = False) -> None:
        self.type = captcha["request_type"]
        self.verbose = verbose
        self.captcha = captcha

    def encode_img(self, url: str, np: bool = False) -> str:
        if np: return cv2.imdecode(numpy.frombuffer(requests.get(url).content, numpy.uint8), cv2.IMREAD_ANYCOLOR)
        else: return base64.b64encode(requests.get(url).content).decode()

    def solve(self) -> dict:
        solvers = {
            'image_drag_drop': self.drag_drop
        }
        try:
            if self.verbose: log.captcha(f"Solving Captcha -> {self.type}...")
            return solvers[self.type]()
        except Exception as e:
            log.failure(f"Failed To Solve {self.type} -> {e}")
            pass

    def drag_drop(self) -> dict:
        start = time.time()
        tasklist = self.captcha['tasklist']
        image = self.encode_img(tasklist[0]["datapoint_uri"], np=True)
        shapes = [{entity["entity_id"]: entity["entity_uri"]} for entity in tasklist[0]["entities"]]
        solution = []
        
        for shapedata in shapes:
            puzzle = self.encode_img(next(iter(shapedata.values())), np=True)
            edge = cv2.Canny(puzzle, 100, 200)
            background = cv2.cvtColor(cv2.Canny(image, 100, 200), cv2.COLOR_GRAY2RGB)
            res = cv2.matchTemplate(background, cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB), cv2.TM_CCOEFF_NORMED)
            top_left = cv2.minMaxLoc(res)[3]
            h, w = edge.shape[:2]
        
            solution.append([top_left[0] + w // 2, top_left[1] + h // 2])
        
        if self.verbose: log.captcha(f"Solved Captcha -> {solution}", start, time.time())
        response = {}
        for i, entity in enumerate(tasklist[0]["entities"]):
            response[tasklist[0]["task_key"]] = response.get(tasklist[0]["task_key"], [])
            response[tasklist[0]["task_key"]].append({
                "entity_name": entity["entity_id"],
                "entity_type": "default",
                "entity_coords": solution[i]
            })
        return response