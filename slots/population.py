def estimates(groups, surveys):
    populations = {row['id']:row['size'] for row in groups}
    result = {}
    for row in surveys:
        key = row['station'],row['group']
        if not 0 <= row['min'] <= row['max'] <= populations[row['group']] or key in result:
            raise ValueError('重复或超出受众组的调查区间')
        result[key] = {'station':key[0],'group':key[1],'min':row['min'],'max':row['max']}
    return [result[key] for key in sorted(result)]
