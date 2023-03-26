import os
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import json
annType = 'bbox'

json_path = '/Users/antonlukanov/Desktop/Sber/model_evaluate/'

true_json = 'coco_dataset/labels.json'
res_json = 'Coco_results/16_09/labels.json'

path_to_annotation = os.path.join(json_path, true_json)

cocoGt = COCO(path_to_annotation)
print(os.path.join(json_path, res_json))

dts = json.load(open(os.path.join(json_path, res_json), 'r'))

cocoDt = cocoGt.loadRes(dts['annotations'])

cocoEval = COCOeval(cocoGt, cocoDt, annType)
cocoEval.params.catIds = [0,1,2,3]

cocoEval.evaluate()
cocoEval.accumulate()

cocoEval.summarize()

mean_ap = cocoEval.stats[0].item()  # stats[0] records AP@[0.5:0.95]
print(mean_ap)
mAP, map50 = cocoEval.stats[:2]
print(mAP, map50)