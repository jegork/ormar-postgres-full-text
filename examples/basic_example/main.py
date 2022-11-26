from examples.basic_example.db.models import FulltextModel, database


async def run():
    await database.connect()
    await FulltextModel.objects.delete(each=True)
    model = FulltextModel(text="hello")
    await model.save()

    await FulltextModel.objects.create(text="hello world")
    await FulltextModel.objects.create(text="one more text")

    # filter using keyword arguments (aka Django style)
    retrieved_models = await FulltextModel.objects.filter(text__match="hello").all()

    print("text_match='hello' results:", retrieved_models)

    # filter using FieldAccessor (aka Pythonic style)
    retrieved_models = await FulltextModel.objects.filter(
        FulltextModel.text.match("text"),
    ).all()
    print("text_match='text' results:", retrieved_models)
    print(retrieved_models[0].text)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
