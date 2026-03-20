import re
from itemadapter import ItemAdapter


class CleanFieldsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        for field in ["job_title", "company_name", "location", "department", "employment_type"]:
            if adapter.get(field):
                adapter[field] = adapter[field].strip()
        return item


class SkillsExtractionPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if not adapter.get("required_skills"):
            adapter["required_skills"] = "Not specified"
        if not adapter.get("salary"):
            adapter["salary"] = "Not specified"
        if not adapter.get("location"):
            adapter["location"] = "Remote"
        if not adapter.get("department"):
            adapter["department"] = "General"
        if not adapter.get("employment_type"):
            adapter["employment_type"] = "Full-time"
        if not adapter.get("experience_level"):
            adapter["experience_level"] = "Mid-level"
        return item