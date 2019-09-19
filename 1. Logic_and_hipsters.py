""" 1 - задание
В лофте n хипстерам достались m смузи. При этом все хипстеры - люди вежливые,
и поэтому должны выпить одинаковое количество смузи (можно выбросить несколько).
Напишите функцию distributeSmoothies(int $m, int $n): int,
результатом которой будет количество смузи, которое выпьет каждый хипстер.
"""

def distributeSmoothies(smuf_num: int, hips_num: int) -> int:
    if smuf_num > hips_num:
        smuf_left = smuf_num - hips_num
        if smuf_left < 5:
            return hips_num
        else:
            return smuf_num // hips_num
    else:
        return smuf_num // hips_num
