from ..models import Group
from ..constants import *
from ...work.y2016 import miao2016a
    
approach = Group(
    miao2016a,
    _category = "Unrelated", # The only paper so far is a technical report
    display="ProvDB",
    approach_name="ProvDB",
    _cite=False,

    _meta=[dict(
        binary=NO,
        languages=[AGNOSTIC, SHELL],

        goal=COMPREHENSION,
        supports=[COMPREHENSION, FRAMEWORK, MANAGEMENT],
        categories=[COLLECTION, EVOLUTION, DIFF, QUERY, FRAMEWORK, STORAGE, VISUALIZATION],

        mode=USER_LEVEL,

        tools=[VCS],
        
        annotations=[EXECUTABLE, EXTERNAL, INCLUSIVE, PROVENANCE],
        execution=[INSTRUMENTATION, POST_MORTEM],
        deployment=[],
        definition=[READING],

        execution_granularity=[INPUT_FILES, OUTPUT_FILES, ARGUMENTS, COMMANDS],
        deployment_granularity=[],
        definition_granularity=[SOURCE, CONTENT],

        cache=NO,
        replay=NO,
        evolution=YES.star("DVCS"),
        pipeline=YES,
        summarization=[],

        distribution=[],
        storage=[GRAPH_DB.such_as(["Neo4j"]), REPOSITORY.such_as(["Git"])],
        visualization=[COMBINED_VIEW, WEB],
        query=[QUERY.such_as(["Cypher"]), WEB],
        integration=[],
        
        granularity=[COMMANDS, ARGUMENTS, INPUT_FILES, OUTPUT_FILES],
        granularity_text="Commands, Arguments, Input and Output files",
        thread=YES,
        diff=YES,
                    
        limitations=[],
    )],
    _about="""
        <p>
            ProvDB (<a href="#miao2016a" class="reference">MIAO; CHAVAN; DESHPANDE, 2016</a>) uses provenance to support <span class="goal"> comprehension </span> of experiments, allowing their bookkeeping and debugging.
            <span class="collection">
                For collecting provenance, it uses extensible provenance ingestion mechanisms.
                The main ingestion mechanism in the system is the shell-based ingestion framework. This mechanism allows users to prepend shell commands with "provdb" to <span title="Matches arguments againts regular expressions: collects arguments">capture their arguments</span> and create <span title="Implicit versions are kept separate from explicit versions created through git commit">implicit versions</span> with output data. Thus, it applies the <span class="strategy"> post-mortem and instrumentation </span> strategies.
            </span>
        </p>
        <p class="collection">
            In addition to the shell-based ingestion mechanism, ProvDB also offers a DVCS ingestion mechanism, that collects versioning information from git. It allows ProvDB to support the evolution of experiments.
            Additionally, ProvDB has a file views mechanism that allows users to create virtual files using simplifies SQL or bash scripts; and a caffe ingestion mechanism for capturing fine-grained information of results generated by the caffe deep learning framework.
            ProvDB also allows users to write annotations as project properties. This allows users to describe usages and explain the rationale of a experiment.
        </p>
        <p class="analysis">
            For analysis, ProvDB offers a web tool that allows users to visualize pipelines, charts, and run cypher queries.
            ProvDB also supports two types of diffs on the provenance: a (i) shallow diff that tries to match properties of two snapshots and presents the differences; and (ii) deep diff that compares ancestors of two target snapshots until it finds a common ancestor
        </p>
        <p class="storage">
            ProvDB users a Neo4j database and a DVCS repository for storing provenance.
        </p>
    """,
)


