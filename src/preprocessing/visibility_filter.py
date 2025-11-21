class VisibilityFilter:
    def __init__(self, min_bbox_area=1500, min_leg_confidence=0.4):
        self.min_bbox_area = min_bbox_area
        self.min_leg_confidence = min_leg_confidence

    def score(self, bbox_area, leg_conf):
        # simple normalized visibility score
        area_score = min(1.0, bbox_area / self.min_bbox_area)
        leg_score = min(1.0, leg_conf / self.min_leg_confidence)
        return (area_score + leg_score) / 2.0

    def keep(self, bbox_area, leg_conf, threshold=0.5):
        # return True if sample is "good enough"
        return self.score(bbox_area, leg_conf) >= threshold
