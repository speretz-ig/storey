from storey import build_flow, Source, Map, Filter, JoinWithTable


def test_functional_flow():
    flow = build_flow([
        Source(),
        Map(lambda x: x + 1),
        Filter(lambda x: x < 3),
        JoinWithTable(lambda x: x, lambda x, y: y['secret'], '/bigdata/gal'),
        Map(lambda x: print(x))
    ])
    mat = flow.run()
    for _ in range(100):
        for i in range(10):
            mat.emit(i)
    mat.terminate()
    mat.await_termination()
