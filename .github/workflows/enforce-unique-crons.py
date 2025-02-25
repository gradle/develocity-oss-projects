import os
import re

def update_cron_schedules(directory):
    cron_base = "0 {} * * {}"
    cron_hour = 1
    cron_day = 4

    for filename in os.listdir(directory):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                content = file.read()

            new_cron = cron_base.format(cron_hour, cron_day)
            updated_content = re.sub(r'    - cron: "0 9 \* \* 0"', f'    - cron: "{new_cron}"', content)

            with open(filepath, 'w') as file:
                file.write(updated_content)

            cron_hour += 1
            if cron_hour > 23:
                cron_hour = 0
                cron_day += 1

if __name__ == "__main__":
    workflows_dir = "/Users/gfeo/p/gradle/develocity-oss-projects/.github/workflows"
    update_cron_schedules(workflows_dir)
